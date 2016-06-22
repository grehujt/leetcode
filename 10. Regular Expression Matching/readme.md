# 10. Regular Expression Matching

### Problem
- Implement regular expression matching with support for '.' and '*'.
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
- The matching should cover the entire input string (not partial).
- The function prototype should be:

```c
bool isMatch(const char *s, const char *p)
```

- Some examples:

```c
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
```
