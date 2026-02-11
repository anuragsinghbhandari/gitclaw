#!/usr/bin/env python3
from ddgs import DDGS
import argparse

def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
        return results
    except Exception as e:
        print(f"Error during web search: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Search the web using DuckDuckGo.")
    parser.add_argument("query", help="The search query.")
    args = parser.parse_args()

    results = search_web(args.query)

    if results:
        print("Search results:")
        for i, result in enumerate(results):
            print(f"[{i+1}] {result['title']}\n  {result['body']}\n  {result['href']}\n")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
