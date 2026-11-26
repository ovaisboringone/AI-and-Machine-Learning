site = {
    'Home': {
        'About': {},
        'Products': {
            'Electronics': {},
            'Books': {}
        },
        'Contact': {}
    }
}

def dfs(tree, target, path):
    for page in tree:
        path.append(page)

        if page == target:
            return path

        result = dfs(tree[page], target, path)

        if result:
            return result

        path.pop()

path = dfs(site, 'Books', [])
print(" -> ".join(path))