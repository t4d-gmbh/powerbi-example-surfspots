# Power BI example with surf spots in Portugal

In this tutorial, we present a basic structure for a Microsoft Power BI data model and a report. 

As an example, we use a public dataset with 129 surf spots in Portugal.

## For beginners
  
.. or other interested people:
  
[t4d-gmbh.github.io/powerbi-example-surfspots](https://t4d-gmbh.github.io/powerbi-example-surfspots)


## For developers

In June 2024 Microsoft launched the [Power BI enhanced report format (PBIR)](https://powerbi.microsoft.com/en-us/blog/power-bi-enhanced-report-format-pbir-in-power-bi-desktop-developer-mode-preview/)
which allows storing an entire Power BI report in structured JSON files. 
This makes it possible to apply automated changes to a report.
In this example, we have created a Git Hook 
[pre-push](https://github.com/t4d-gmbh/powerbi-example-surfspots/blob/main/scripts/pre-push) 
 that executes all python scripts in the 
[scripts](https://github.com/t4d-gmbh/powerbi-example-surfspots/tree/main/scripts) folder. The script 
[hide_visual_filters.py](https://github.com/t4d-gmbh/powerbi-example-surfspots/blob/main/scripts/hide_visual_filters.py)
sets all visual filters to hidden. More scripts can be added, such as apply default filter settings.
The following diagram shows the development process when working with the Git Hook:
  
  
![Git Hook pre-push workflow](https://raw.githubusercontent.com/t4d-gmbh/powerbi-example-surfspots/main/doc/figures/git-pre-push-workflow.drawio.png)
  
  
To activate the Git Hook, copy the file *scripts/pre-push* to *.git/hooks/pre-push* in your local repository.
Python 3 must be installed on your local machine. Instead of python, you can create your own scripts with *PowerShell* or another scripting language.
  
The *Power BI enhanced report format (PBIR)* is still in preview mode and does not yet work in every detail. 
As soon as it is fully ready, it will significantly improve Power BI development.


