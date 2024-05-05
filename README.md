# db-ml-final-project-cs133sp24-sjsu

Team: Jonathan Manzano &amp; Henry Pham  
Dataset: Autism in children  
Row Count: 292  
Column Count: 21

**What is this data?:** This dataset contains records of children who have answered the 10 behaviors questions (AQ-10-Child Question) and 10 of their characteristics. The questions and the characteristics are used to determine whether the child may or may not have autism.

**DataSet:**

| Column_name     | datatype | Description                                                                                                                    |
|-----------------|----------|--------------------------------------------------------------------------------------------------------------------------------|
| A1_Score        | int64    | AQ-10-Child Question 1 Answer Binary (0, 1)                                                                                    |
| A2_Score        | int64    | AQ-10-Child Question 2 Answer Binary (0, 1)                                                                                    |
| A3_Score        | int64    | AQ-10-Child Question 3 Answer Binary (0, 1)                                                                                    |
| A4_Score        | int64    | AQ-10-Child Question 4 Answer Binary (0, 1)                                                                                    |
| A5_Score        | int64    | AQ-10-Child Question 5 Answer Binary (0, 1)                                                                                    |
| A6_Score        | int64    | AQ-10-Child Question 6 Answer Binary (0, 1)                                                                                    |
| A7_Score        | int64    | AQ-10-Child Question 7 Answer Binary (0, 1)                                                                                    |
| A8_Score        | int64    | AQ-10-Child Question 8 Answer Binary (0, 1)                                                                                    |
| A9_Score        | int64    | AQ-10-Child Question 9 Answer Binary (0, 1)                                                                                    |
| A10_Score       | int64    | AQ-10-Child Question 10 Answer Binary (0, 1)                                                                                   |
| age             | object   | Age Number                                                                                                                     |
| gender          | object   | Gender Male (m) or Female (f)                                                                                                  |
| ethnicity       | object   | Ethnicity                                                                                                                      |
| jundice         | object   | Born with jaundice Boolean (yes or no)                                                                                         |
| austim          | object   | Whether any immediate family member has a Pervasive developmental disorder (yes or no)                                         |
| country_of_res  | object   | Country of residence                                                                                                           |
| used_app_before | object   | Whether the user has used a screening app (yes or no)                                                                          |
| total_score     | int64    | Sum of scores from the 10 questions. If the individual scores 6 or above, they should seek a specialist diagnostic assessment. |
| age_desc        | object   | age range                                                                                                                      |
| relation        | object   | Who is completing the test String Parent, self, caregiver, medical staff, clinician, etc.                                      |
| ASD             | object   | Case of autism (YES or NO)                                                                                                     |

1. What are you going to be predicting?  
Machine learning on this dataset will try to predict whether a child has autism spectrum disorder (ASD) by looking at the relation between diagnosed ASD and the scores provided in the dataset, will try to factor in regional differences to account for cultural differences when diagnosing children with ASD.  

2. What geographical-based information are you going to use (or can you add) for the map visualization?  
There is already a region column in the dataset, so we will use that.
