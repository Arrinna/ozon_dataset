# Issues Log

## 1. Duplicate Category Names
- **Description:**
  - The name of the category (used as a file name and as the 'Category' column in the merged dataset) can be duplicated within different parent categories. For example, 'Accessories' may appear in multiple parent categories.
- **Impact:**
  - This can cause ambiguity when merging or analyzing data, as different files with the same category name may overwrite each other or be indistinguishable in the merged dataset.
- **Potential Solution:**
  - Use a more specific identifier for the category, such as including the parent category in the file name or in the 'Category' column (e.g., 'ParentCategory-Accessories'). 