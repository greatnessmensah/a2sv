class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitted = path.split("/")
        
        for path in splitted:
            if path == "." or path == "":
                continue
            elif path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
                
        return "/" + "/".join(stack)