# RegTech
Capstone Project - DAEN 690

## About
Requirements capture in large financial regulatory and compliance documents is a strenuous, time consuming, and a costly task. The current approach to regulatory compliance by the financial services industry is manual and labor intensive which makes the whole process costly in terms of time and money. Additionally, there aren’t enough people that qualify to be compliance professionals. In wake of ever increasing volume of data and an increase in expectations of compliance responsibilities, it is essential to streamline this task by reducing the amount of work significantly. This project proposes an approach to achieve that goal by applying Natural Language Processing and Text Mining to extract requirements and their concepts (RDF triples). Furthermore, this project outlines a comprehensive way to get human input to determine the authenticity of the requirements and then to display the findings in an executive dashboard

## Structure

The folder **RegTechInterface** has the code for the front-end which is used by the compliance officers to approve/disapprove a requirement.

The folder **PythonCode** has the code for the scraping regulations from U.S Federal Government website and storing them in a SQL database. 
The file **NLTK_Capstone_FinalVersion** has code where all the processing is being done on the text scraped.

## Screenshots

### Dashboard
The following dashboard gives the user an overview of all the requirements; the chapter it is from along with how many compliance officers approve of the requirement. 

It also shows the developers information related to this particular project on how well the project performed.  

