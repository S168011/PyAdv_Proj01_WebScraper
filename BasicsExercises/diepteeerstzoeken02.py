folder_hierarchy = {
    "name": "level 1 directory",
    "children": [
        {
            "name": "level 2 directory A",
            "children": [
                {"name": "level 3 directory A1", "children": []},
                {"name": "level 3 directory A2", "children": []},
            ],
        },
        {
            "name": "level 2 directory B",
            "children": [ {"name": "level 3 directory B1", "children": []} ],
        },
        {
            "name": "level 2 directory C",
            "children": [
                {"name": "level 3 directory C1", "children": []},
                {"name": "level 3 directory C2", "children": []},
                {"name": "level 3 directory C3", "children": []},
            ],
        },
    ],
}

def recursive(data: dict, indent: int) -> None:
    for key in data:
        if key == "name":
            print("    " * indent + data["name"])
    
    for child in data[key]:
        recursive(child, indent + 1)

def main():
    recursive(folder_hierarchy, 0)

if __name__ == "__main__":
    main()