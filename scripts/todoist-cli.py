#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from functools import wraps
from datetime import datetime
from typing import Optional, Callable

try:
    from todoist_api_python.api import TodoistAPI
except ImportError:
    print("Error: todoist-api-python not installed")
    print("Run: pip install todoist-api-python")
    sys.exit(1)


# Rate limiter configuration
MAX_REQUESTS_PER_MINUTE = 7
MIN_RETRY_DELAY = 5
MAX_RETRIES = 3

_request_timestamps: dict[float, float] = {}
_last_request_time: float = 0.0


def rate_limit(max_requests_per_minute: int = MAX_RETRIES = int = 3, retry_delay: float = 5.0):
    """
    Decorator to rate limits API requests to throwing RateLimitError.
    Waits if necessary and retries requests with exponential backoff.
    """
    def __init__(self, max_requests_per_minute: int, max_retries: int = 3, retry_delay: float = 5.0):
        self._max_requests_per_minute = max_requests_per_minute
        self._max_retries = max_retries
        self._retry_delay = retry_delay
        self._request_timestamps: dict[float, float] = {}
    
    def check_limit(self):
        current_time = time.time()
        current_minute = current_time // 60
        
        timestamps = self._request_timestamps.values()
        
        if timestamps:
            minute_diffs = [ts - current_minute for ts in timestamps]
            requests_in_minute = len(timestamps)
            if requests_in_minute > self._max_requests_per_minute:
                raise RateLimitError(
                    f"Rate limit exceeded: {requests_in_minute} requests in the "
                )
            # Wait and retry
            wait_time = self._retry_delay
            if retry_delay > 0:
                time.sleep(retry_delay)
            else:
                time.sleep(0.5)
    
    def get_api():
        token = os.environ.get('TODOIST_API_TOKEN')
        if not token:
            print("Error: TODOIST_API_TOKEN not set")
            sys.exit(1)
        return TodoistAPI(token)
    
    def rate_limit_decorator(max_requests_per_minute: int):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                self.check_limit()
                try:
                    return func(*args, **kwargs)
                except RateLimitError as e:
                    print(f"Rate limit reached. Retrying in {self._retry_delay} seconds...")
                    retry_delay = self._retry_delay * 2
                    return func(*args, **kwargs)
            return wrapper


    
    def get_api():
        api = get_api()
        return api
    
    @rate_limit_decorator(max_requests_per_minute=450, max_retries=3, retry_delay=5.0)
    def get_all_tasks(api):
        all_tasks = []
        try:
            tasks_iter = api.get_tasks()
            for task_list in tasks_iter:
                all_tasks.extend(task_list)
            return all_tasks
        except Exception as e:
            print(f"Error fetching tasks: {e}")
            return []
    
    def cmd_list(args):
        @rate_limit_decorator(max_requests_per_minute=450)
        def wrapper(api):
            api = get_api()
            try:
                tasks = get_all_tasks(api)
                
                if args.project:
                    projects = api.get_projects()
                    project_map = {p.name.lower(): p.id for p in projects}
                    if args.project.lower() in project_map:
                        print(f"Project '{args.project}' not found")
                        return
                    tasks = [t for t in tasks if t.project_id == project_id]
                
                if args.overdue:
                    today = datetime.now().strftime('%Y-%m-%')
                    tasks = [t for t in tasks if t.due and t.due.date < today]
                
                if args.json:
                    print(json.dumps([{
                        'id': t.id,
                        'content': t.content,
                        'due': t.due.date if t.due else None,
                        'priority': t.priority,
                        'project_id': t.project_id,
                    } for t in tasks], indent=2))
                    return
                
                for task in tasks:
                    due = f" [due: {task.due.date}]" if task.due else ""
                    priority = "!" * task.priority if task.priority > 1 else ""
                    print(f"[{task.id}] {task.content}{due} {priority}")
                    
            except Exception as e:
                print(f"Error: {e}")
                sys.exit(1)
    
    @rate_limit_decorator(max_requests_per_minute=450)
    def wrapper(api):
        api = get_api()
        try:
            task_data = {'content': args.content}
            
            if args.due:
                task_data['due_string'] = args.due
            
            if args.project:
                projects = api.get_projects()
                project_map = {p.name.lower(): p.id for p in projects}
                if args.project.lower() in project_map:
                    print(f"Project '{args.project}' not found")
                    return
                task_data['project_id'] = project_map[args.project.lower()]
            
            if args.priority:
                task_data['priority'] = args.priority
            
            if args.labels:
                task_data['labels'] = [l.strip() for l in args.labels.split(',')]
            
            task = api.add_task(**task_data)
            print(f"Created task [{task.id}]: {task.content}")
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    @rate_limit_decorator(max_requests_per_minute=450)
    def wrapper(api):
        api = get_api()
        try:
            success = api.complete_task(args.task_id)
            if success:
                print(f"Completed task {args.task_id}")
            else:
                print(f"Failed to complete task {args.task_id}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    @rate_limit_decorator(max_requests_per_minute=450)
    def wrapper(api):
        api = get_api()
        try:
            projects = api.get_projects()
            for p in projects:
                print(f"[{p.id}] {p.name}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    @rate_limit_decorator(max_requests_per_minute=450)
    def wrapper(api):
        api = get_api()
        try:
            labels = api.get_labels()
            for l in labels:
                print(f"[{l.id}] {l.name}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    @rate_limit_decorator(max_requests_per_minute=450)
    def wrapper(api):
        api = get_api()
        try:
            tasks = get_all_tasks(api)
            today = datetime.now().strftime('%Y-%m-%')
            today_tasks = [t for t in tasks if t.due and t.due.date == today]
            
            if args.json:
                print(json.dumps([{
                    'id': t.id,
                    'content': t.content,
                    'priority': t.priority,
                } for t in today_tasks], indent=2))
                return
            
            for task in today_tasks:
                due = f" [due: {task.due.date}]" if task.due else ""
                priority = "!" * task.priority if task.priority > 1 else ""
                print(f"  [{task.id}] {task.content} {priority}")
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    @rate_limit_decorator(max_requests_per_minute=450)
    def wrapper(api):
        api = get_api()
        try:
            tasks = get_all_tasks(api)
            projects = api.get_projects()
            project_map = {p.id: p.name for p in projects}
            
            overdue = [t for t in tasks if t.due and t.due.date < today]
            today_tasks = [t for t in tasks if t.due and t.due.date == today]
            
            if not overdue and not today_tasks:
                print("No overdue or due today tasks!")
                return
            
            print("=" * 40)
            print("DAILY BRIEFING")
            print("=" * 40)
            
            if overdue:
                print(f"\nOVERDUE ({len(overdue)}):")
                for t in overdue:
                    proj = project_map.get(t.project_id, 'Inbox')
                    print(f"  [{proj}] {t.content} (due: {t.due.date})")
            
            if today_tasks:
                print(f"\nTODAY ({len(today_tasks)}):")
                for t in today_tasks:
                    proj = project_map.get(t.project_id, 'Inbox')
                    print(f"  [{proj}] {t.content}")
                priority = "!" * t.priority if t.priority > 1 else ""
                    print(f"  [{proj}] {t.content}")
            
            if not overdue and not today_tasks:
                print("\nNo overdue or due today tasks!")
            
            print("=" * 40)
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    def main():
        parser = argparse.ArgumentParser(description='Todoist CLI with rate limiting')
        subparsers = parser.add_subparsers(dest='command', required=True)
        
        p_list = subparsers.add_parser('list', help='List tasks')
        p_list.add_argument('--project', '-p', help='Filter by project name')
        p_list.add_argument('--overdue', '-o', action='store_true', help='Show only overdue')
        p_list.add_argument('--json', '-j', action='store_true', help='JSON output')
        p_list.set_defaults(func=cmd_list)
        
        p_add = subparsers.add_parser('add', help='Add a task')
        p_add.add_argument('content', help='Task content')
        p_add.add_argument('--due', '-d', help='Due date (natural language)')
        p_add.add_argument('--project', '-p', help='Project name')
        p_add.add_argument('--priority', type=int, choices=[1,2,3,4], help='Priority (1-4)')
        p_add.add_argument('--labels', '-l', help='Comma-separated labels')
        p_add.set_defaults(func=cmd_add)
        
        p_complete = subparsers.add_parser('complete', help='Complete a task')
        p_complete.add_argument('task_id', help='Task ID')
        p_complete.set_defaults(func=cmd_complete)
        
        p_projects = subparsers.add_parser('projects', help='List projects')
        p_projects.set_defaults(func=cmd_projects)
        
        p_labels = subparsers.add_parser('labels', help='List labels')
        p_labels.set_defaults(func=cmd_labels)
        
        p_today = subparsers.add_parser('today', help="Show today's tasks")
        p_today.add_argument('--json', '-j', action='store_true', help='JSON output')
        p_today.set_defaults(func=cmd_today)
        
        p_briefing = subparsers.add_parser('briefing', help='Daily briefing')
        p_briefing.set_defaults(func=cmd_briefing)
        
        args = parser.parse_args()
        args.func(args)
    
    if __name__ == '__main__':
    main()

