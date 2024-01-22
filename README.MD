
## Obsidian Bubble Trainer

---


https://github.com/matthewscullydev/obsidian_bubble_trainer/assets/26017402/591dc682-0536-4b29-8c83-4d2b85913cf3


Given an obsidian markdown file path this program will turn every reference into a string of question marks.

This will be done starting at the first reference and ending at the last

The user will be asked which set of question marks responds to which reference sequentially until all references have been resolved.


Once all references have been resolved the user will recieve the following statistics on their performance.

    - Retention Rate
    - Speed


### Free Mode

---

If the user enters free mode every reference will be turned into a string of question marks.

The user will not be asked to resolve any references. It will be up to them to enter values that resolve references.

For every string input that matches a reference will be resolved.

If the user finishes all references statistics for performance will be returned

otherwise the user can press F to finish and all references will be resolved and statstics will be returned.



### Saving and Seperating Mental Maps

---

To keep the graph view clear while maintaining your collection of mind maps you should do the following:

mkdir name_of_subject
mv *.md name_of_subject

Then in the Obsidian Files and Links settings find the setting which says Excluded Files and select name_of_subject/

This allows you to create and preserve mental maps while keeping your graph view tidy.

In order to use these maps again in graph view simply move all files out of the subfolder you created back into the main folder with:

cd name_of_subject; mv *.md ../

