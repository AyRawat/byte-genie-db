# byte-genie-db


# Database Schema

## Tables

### `company`
| Column Name     | Data Type     | Description                               |
|-----------------|---------------|-------------------------------------------|
| `company_id`    | INTEGER       | Primary key, unique identifier for each company |
|`company_logo_url`|VARCHAR(255) | Logo of the company|
|`company_logo_text`|VARCHAR(255) | text in the logo|
|`relation_to_event`|VARCHAR(255) | Relation to the event |
|`company_phone`|VARCAHR(255)| Phone Number |
|`company_founding_year`|VARCHAR(255) |When  company was founded|
|`company_industry`|VARCHAR(255)| Industry to which company is related to|
| `company_name`  | VARCHAR(255)  | Name of the company                       |
| `company_revenue` | FLOAT     | Revenue of the company                    |
| `n_employees`   | FLOAT         | Number of employees                       |
| `event_url`     | VARCHAR(255)  | URL of the related event                  |
| `homepage_base_url` | VARCHAR(255) | Homepage URL of the company              |
|`company_overview`|VARCHAR(255)| The overview of the company|


### `event`
| Column Name        | Data Type     | Description                                  |
|--------------------|---------------|----------------------------------------------|
| `event_id`         | INTEGER       | Primary key, unique identifier for each event |
| `event_name`       | VARCHAR(255)  | Name of the event                            |
| `event_description`| TEXT          | Description of the event                     |
| `event_url`        | VARCHAR(255)  | URL of the event                             |
| `event_industry`   | VARCHAR(255)  | Industry of the event                        |
| `event_start_date` | DATE          | Start date of the event                      |
| `event_end_date`   | DATE          | End date of the event                        |
| `event_country`    | VARCHAR(255)  | Country where the event is held              |                        |
| `event_industry`    | VARCHAR(255)  | The type of industry that this event is catering to        |


### `people`
| Column Name        | Data Type     | Description                                  |
|--------------------|---------------|----------------------------------------------|
| `person_id`        | INTEGER       | Primary key, unique identifier for each person |
| `first_name`       | VARCHAR(255)  | First name of the person| 
| `middle_name`       | VARCHAR(255)  | Middle name of the person                        | 
| `last_name`        | VARCHAR(255)  | Last name of the person                      |
| `job_title`       | VARCHAR(255)  | Job Title of the person|   
| `person_city`        | VARCHAR(255)  | City where the person is living|
| `person_state`        | VARCHAR(255)  | State where the person is living|
| `person_country`        | VARCHAR(255)  | Country where the person is living|
| `homepage_base_url`| VARCHAR(255)  | Homepage URL of the company the person works for |                 
|  `duration_in_current_job`        | VARCHAR(255)  | Duration of current job|
| `duration_in_current_company`        | VARCHAR(255)  | Duration of current company|
| `email`| VARCHAR(255)  | Email of the person |


## Relationships
- **One-to-Many**: `company` to `event` (a company can be associated with multiple events)
- **One-to-Many**: `people` to `company` (a person can work for one company)

## Sample Queries

### Get all companies with more than 100 employees:
```sql
SELECT company_name 
FROM company 
WHERE CAST(n_employees AS INTEGER) > 100;
```







## Problems faced.
1. Figuring out the important columns and fixing the inconsistencies of the Raw data
2. Mapping industry was the most difficult part. I first had to get unique industries from the company_industry table. Then I had to use my model to identify the industry of the event using event_name and event_overview, at last I chose the relevant industry from the list that I acquired earlier.
3. Missing data in fields like phone number , revenue and employees etc.
4. Heterogeneous format of the data in company_revenue and n_employees like  11-50, 420.0 or 10001 employees
5. Missing fields like email of the employee and industry of the event that it is related to.
6. Fields that are not in Normalized formats , comapny_industry . A company can 
have multiple industries.


## Improvement
One thing that I would have definitely improved upon was the normalization of company_industry column. It had multiple values and sometimes duplicate as well. 
 I would have created two new tables, One containing the industries and the ids . and one table, just for acting as the bridge between two. which would have contained company_id and industry_id, to which the company is related to.
 Due to the restrictions on my model usage, I couldn't divide it and Ihad to go with the LIKE query.

 Other thing would be to remove the unnecessary columns like company_logo_url and text.


