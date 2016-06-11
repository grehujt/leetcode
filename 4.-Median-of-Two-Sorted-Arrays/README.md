## Median of Two Sorted Arrays

> There are two **sorted** arrays nums1 and nums2 of **size** m and n respectively. 
>
> Find the median of the two sorted arrays.
>
> The overall run time complexity should be O(log (m+n)).

---

### analysis

- setups
  - We have 2 sorted lists, L1 and L2.
  - L1 has m elements, and L2 has n elements, m and n can be different. 
  - Our goal is to find the median of the union of L1 and L2.
  - O(log(m+n)) time complexity algorithm is required.

- O(m+n) solution
  Using merge part of the merge sort, we can easily get a O(n) solution by first building a sorted union of L1 and L2 in O(n) then return the median of it. And its space complexity is O(n).
  Or we can just use two pointers to iterate L1 and L2 correspondingly, and by comparing the values we can know the final positions of the elements in the union list. This approach reduces the space complexity to O(1).
- O(log(m+n)) solution
  - At first glance, T(n) = T(n/2) + O(1) will give us a O(log(n)) solution, so it hints us to use some greedy  strategies to drop half elements each time, and we are not going to do more than O(1) extra stuff.
  - If we want to solve a problem elegently, we need to understand it very well. Median of a sorted list of numbers, is the middle point of the list, which separates the list into two parts with equal length. 
  - Based on the first part of the above O(m+n) solution, if we can build the union of L1 and L2 in O(log(m+n)), we are done. But we cannot. 
  - However, the second part of above O(m+n) solution also hints us to count, if we can count the final position of elements in the union of L1 and L2 in O(log(m+n)) without creating the union, we are solving this in O(log(m+n)) as well. And in this case, we can!!!
