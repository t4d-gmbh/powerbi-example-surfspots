# Introduction


## Idea

In this tutorial, we present a basic setup for a Microsoft Power BI data model and one report page. 
As an example, we use a public dataset with 129 surf spots in Portugal.[^sn1]


[^sn1]: [Principais Spots de Surf (dados.gov.pt)](https://dados.gov.pt/pt/datasets/principais-spots-de-surf-3/) 


```{note}
We present some concepts that have proven useful in our practical work. 
However, there are many different ways to implement a certain functionality in Power BI. 

This is not a typical beginner's guide in which all concepts are explained from scratch. There are already plenty of helpful websites for beginners, like the 
official article from microsoft.com *Get started with Power BI Desktop*[^sn2] or the *Power BI Tutorial for Beginners*[^sn3] from datacamp.com.
```

[^sn2]: [Get started with Power BI Desktop (microsoft.com)](https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started)
 
[^sn3]: [Power BI Tutorial for Beginners](https://www.datacamp.com/tutorial/tutorial-power-bi-for-beginners)


## Key features

This Power BI data model and report have the following key features:

 - Dynamic multilingualism of (almost) the entire report
 - User can change the legend of the map
 - User can choose a measure for the bar chart on the right side

 
## The report

In *Filters on all pages* the user can choose the preferred language. 
The selected options (region and website) in the slicer are combined with an AND operator. 
More information you will find on the page *The report* of this tutorial.

![Power BI Report](figures/powerbi-example-report.png)


## Microsoft Fabric
In 2023 Microsoft launched the data analytics platform *Microsoft Fabric* and Power BI is a part of it. 
The Power BI Architecture itself consists of several components. A short description of each component you find in the article
*Components of Power BI Architecture*[^sn4].
To keep this tutorial simple, we will focus on the *Power BI Desktop*[^sn5] software, which can be downloaded for free. 

```{note}
If you want to share a report with other users in your organization, you have to publish the report to Power BI Service, 
a cloud service from Microsoft. See article *What is the Power BI Service?*.[^sn6]
For *Power BI Service* you (or your organization) need a *Power BI PRO* or *Power BI Premium* license.[^sn7]
Keep in mind that with the *Power BI PRO* license the *Model memory size limit* is 1GB (the size of the *.pbix file).
```


[^sn4]: [Components of Power BI Architecture (medium.com)](https://medium.com/@theknowledgeacademy/components-of-power-bi-architecture-d12dd18acf41)

[^sn5]: [Power BI Desktop](https://powerbi.microsoft.com/en-us/desktop/)

[^sn6]: [What is the Power BI service?](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-service-overview)

[^sn7]: [Power BI pricing](https://powerbi.microsoft.com/en-us/pricing/)


 




