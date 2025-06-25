import ast
import os


def load_fetch_function():
    path = os.path.join(os.path.dirname(__file__), '..', 'DISCORD BOT', 'bot.py')
    with open(path, 'r') as f:
        source = f.read()
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == 'fetchurlcorectly':
            mod = ast.Module(body=[node], type_ignores=[])
            namespace = {}
            exec(compile(mod, filename='<ast>', mode='exec'), namespace)
            return namespace['fetchurlcorectly']
    raise RuntimeError('function not found')


def test_trailing_slash_removed():
    func = load_fetch_function()
    func.__globals__['domain'] = 'https://example.com/'
    assert func() == 'https://example.com'


def test_no_trailing_slash_unchanged():
    func = load_fetch_function()
    func.__globals__['domain'] = 'https://example.com'
    assert func() == 'https://example.com'
