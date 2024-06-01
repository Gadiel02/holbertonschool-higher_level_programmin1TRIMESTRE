#!/usr/bin/python3
"""API Request module"""
import requests
import csv

def fetch_and_print_posts():
    """Requests Post data from JSONPlaceholder"""
    post_data = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {post_data.status_code}")
    if 200 <= post_data.status_code < 300:
        for post in post_data.json():
            print(post["title"])

def fetch_and_save_posts():
    """Requests Post data from JSONPlaceholder"""
    post_data = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {post_data.status_code}")
    if 200 <= post_data.status_code < 300:
        new_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in post_data.json()
        ]
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', "w", encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_data)

# Example usage
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
