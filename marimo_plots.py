import marimo

__generated_with = "0.5.0"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        # DASHBOARD PROJECT

        ## Team: Jonathan Manzano & Henry Pham  

        **Dataset**: Autism in Children  
        """
    )
    return


@app.cell
def __():
    import pandas as pd
    import os
    import plotly.express as px
    import plotly.graph_objects as go
    return go, os, pd, px


@app.cell
def __(pd):
    def get_data():
        data="https://raw.githubusercontent.com/csbfx/cs133/main/autism_child.csv"
        df = pd.read_csv(data, sep=',', na_values = '?')
        return df

    autism_df = get_data()
    return autism_df, get_data


@app.cell
def __():
    indiv_scores = ["A1_Score",	"A2_Score",	"A3_Score",	"A4_Score",	"A5_Score",	"A6_Score",	"A7_Score",	"A8_Score",	"A9_Score",	"A10_Score"]
    return indiv_scores,


@app.cell
def __(autism_df, mo):
    mo.md(
        f"""
        ## {mo.accordion({"Autism Dataset" : autism_df})}
        """
    )
    return


@app.cell
def __(mo, q1):
    mo.md(
        f"""
        ## What is the distribution of ASD cases across different countries?  
        {mo.accordion({"Click me !": q1})}
        """
    )
    return


@app.cell
def __(mo, plot1):
    # add plot descrips here @line6
    q1 = mo.md(
        f"""
        {plot1}


        
        """
    )
    return q1,


@app.cell
def __(autism_df, mo, px):
    # Filter data for ASD cases
    asd_cases = autism_df[autism_df['ASD'] == 'YES']

    # Count the number of ASD cases per country
    asd_count_by_country = asd_cases['country_of_res'].value_counts().reset_index()
    asd_count_by_country.columns = ['country', 'count']

    # Create the choropleth map
    _fig = px.choropleth(asd_count_by_country,
                        locations="country",
                        locationmode='country names',
                        color="count",
                        hover_name="country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title='Global Distribution of ASD Cases')

    _config = {
       # 'autosize': True,
        'scrollZoom': True,
              }

    # _fig.show() replace with below statement
    plot1 = mo.ui.plotly(_fig, config = _config)
    return asd_cases, asd_count_by_country, plot1


@app.cell
def __(mo, q2):
    mo.md(
        f"""
        ## How does the Total ASD Screening Score vary by Gender, Jaundice, Family History of Autism, or Screening History?  
        
        {mo.accordion({"Find out !":q2})}
        """
    )
    return


@app.cell
def __(box_plots_dropdown, mo):
    # add plot descrips here @line9
    q2 = mo.md(
        f"""
        ## Distribution of Scores by:  
        {box_plots_dropdown}

        {box_plots_dropdown.value}



        """
    )
    return q2,


@app.cell
def __(
    family_history_box_plot,
    gender_box_plot,
    jaundice_box_plot,
    mo,
    screening_box_plot,
):
    box_plots_dropdown = mo.ui.tabs(
        tabs=dict(

                {
                '💪 Gender           ': gender_box_plot,
                '😮 Jaundice         ': jaundice_box_plot,
                '👫 Family History   ': family_history_box_plot,
                '📑 Screening History': screening_box_plot
                }.items()

        ),
        value = 'Gender'
    )
    return box_plots_dropdown,


@app.cell
def __(autism_df, px):
    # Create a box plot to visualize the distribution of total scores by gender
    _fig = px.box(autism_df, x='gender', y='total_score', 
                 points="all",  # This option shows all points (outliers)
                 title='Distribution of Total ASD Screening Scores by Gender',
                 labels={'total_score': 'Total ASD Screening Score', 'gender': 'Gender'},
                 color='gender'
                 )  # Color by gender to distinguish easily

    _fig.update_layout(
        xaxis_title='Gender',
        yaxis_title='Total ASD Screening Score',
        legend_title=" ",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)
    )

    # _fig.show() replace with below statement
    gender_box_plot = _fig
    return gender_box_plot,


@app.cell
def __(autism_df, px):
    # Create a box plot to visualize the distribution of total scores by jaundice
    _fig = px.box(autism_df, x='jundice', y='total_score', 
                 points="all",  # This option shows all points (outliers)
                 title='Distribution of Total ASD Screening Scores by Jaundice',
                 labels={'total_score': 'Total ASD Screening Score', 'jundice': 'Jaundice'},
                 color='jundice',
                 color_discrete_sequence=px.colors.qualitative.T10, 
                 category_orders= {"jundice": ["yes", "no"]})  # Color by jundice to distinguish easily

    _fig.update_layout(
        xaxis_title='Jaundice at Birth',
        yaxis_title='Total ASD Screening Score',
        legend_title=" ",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)
    )

    # _fig.show() replace with below statement
    jaundice_box_plot = _fig
    return jaundice_box_plot,


@app.cell
def __(autism_df, px):
    # Create a box plot to visualize the distribution of total scores by screening history
    _fig = px.box(autism_df, x='used_app_before', y='total_score', 
                 points="all",  # This option shows all points (outliers)
                 title='Distribution of Total ASD Screening Scores by Screening History',
                 labels={'total_score': 'Total ASD Screening Score', 'used_app_before': 'Screening History'},
                 color='used_app_before',
                 category_orders= {"used_app_before": ["yes", "no"]})  # Color by Screening History to distinguish easily

    _fig.update_layout(
        xaxis_title='Screening History',
        yaxis_title='Total ASD Screening Score',
        legend_title=" ",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)

    )

    # _fig.show() replace with below statement
    screening_box_plot = _fig
    return screening_box_plot,


@app.cell
def __():
    ## history_box_plot is linked with another cell
    return


@app.cell
def __(mo, q3):
    mo.md(
        f"""
        ## Is there a relationship between the ASD Screening Outcomes and _____ ?

        {mo.accordion({"Look here !": q3})}

        wowowowow
        asdfgsdg
        sdg
        sd
        gs
        g
        sgd
        sdg
        s
        gs
        dgs
        g
        
        """
    )
    return


@app.cell
def __(bar_plot_options, mo):
    # add plot descrips here @line 9
    q3 = mo.md(
        f"""
        ## Relationship between:  
        {bar_plot_options}  

        {bar_plot_options.value}

        
        
        """
    )
    return q3,


@app.cell
def __(family_history_bar_plot, jaundice_bar_plot, mo, screening_bar_plot):
    bar_plot_options = mo.ui.tabs(
        tabs=dict(
            
                {
                    "😮 Jaundice         ": jaundice_bar_plot,
                    "👫 Family History   ": family_history_bar_plot,
                    "📑 Screening History": screening_bar_plot
                }
            
        )
    )

    bar_config = {
        'displayModeBar': False
    }
    return bar_config, bar_plot_options


@app.cell
def __(autism_df, px):
    # family history bar & box plot

    _autism_df = autism_df.copy()
    # Create a new column for simplicity in plotting
    _autism_df['family_history'] = autism_df['austim'].apply(lambda x: 'With Family History' if x == 'yes' else 'No Family History')

    # Create a stacked bar chart to visualize the relationship between family history and ASD outcomes
    _fig = px.bar(_autism_df, x='family_history', color='ASD', 
                 title='Relationship Between Family History of Autism and ASD Diagnosis',
                 labels={'family_history': 'Family History of Autism', 'ASD': 'ASD Screening Outcome'},
                  barmode='group',
                  category_orders={"family_history": ["With Family History", "No Family History"], "ASD": ["YES", "NO"]},
                 color_discrete_sequence=px.colors.qualitative.T10
                 )

    _fig.update_layout(
        xaxis_title='Family History of Autism',
        yaxis_title='Count of ASD Outcomes',
        legend_title="ASD Diagnosis",
        yaxis_range=[0,130],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)
    )

    # _fig.show() replace with below statement
    family_history_bar_plot = _fig

    # box plot

    _fig = px.box(_autism_df, x='family_history', y = 'total_score', color='family_history', 
                 title='Distribution of Total ASD Screening Scores by Family History of ASD', 
                  points = 'all',
                 labels={'family_history': 'Family History of Autism', 'total_score': 'Total ASD Screening Score',},
                  category_orders={"family_history": ["With Family History", "No Family History"]}) 

    _fig.update_layout(
        legend_title=" ",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)
    )

    family_history_box_plot = _fig
    return family_history_bar_plot, family_history_box_plot


@app.cell
def __(autism_df, px):
    # jaundice history bar plot
    # Create a grouped bar chart to visualize the relationship between jaundice and ASD outcomes
    _fig = px.bar(autism_df, x='jundice', color='ASD', barmode='group',
                 title='Relationship Between Jaundice at Birth and ASD Diagnosis',
                 labels={'jundice': 'Jaundice at Birth', 'ASD': 'ASD Diagnosis Outcome'},
                 category_orders={"jundice": ["yes", "no"], "ASD": ["YES", "NO"]})  # Ensure consistent order

    _fig.update_layout(
        xaxis_title='Jaundice at Birth',
        yaxis_title='Count of ASD Outcomes',
        legend_title="ASD Diagnosis",
        yaxis_range=[0,130],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)
    )
    # _fig.show()
    jaundice_bar_plot = _fig
    return jaundice_bar_plot,


@app.cell
def __(autism_df, px):
    # Screening history bar plot

    # Create a grouped bar chart to visualize the relationship between Screening App History and ASD outcomes
    _fig = px.bar(autism_df, x='jundice', color='ASD', barmode='group',
                 title='Relationship Between Screening History and ASD Diagnosis',
                 labels={'used_app_before': 'Screening History', 'ASD': 'ASD Diagnosis Outcome'},
                 category_orders={"used_app_before": ["yes", "no"], "ASD": ["YES", "NO"]})  # Ensure consistent order

    _fig.update_layout(
        xaxis_title='Used a Screening App Before',
        yaxis_title='Count of ASD Outcomes',
        legend_title="ASD Diagnosis",
        yaxis_range=[0,130],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1)
    )
    # _fig.show()
    screening_bar_plot = _fig
    return screening_bar_plot,


@app.cell
def __(mo, q4):
    mo.md(
        f"""
        ## What is the distribution of Scores based on the Age of an invdividual who has or has not used a Screening App before?

        {mo.accordion({"Plot it !": q4})}
        """
    )
    return


@app.cell
def __(age_line_plot, mo):
    # add plot descrips here @line 6
    q4 = mo.md(
        f"""
        {mo.as_html(age_line_plot)}  


        
        """
    )
    return q4,


@app.cell
def __(autism_df, px):
    _score_age_distribution = autism_df.groupby(['age', 'total_score']).size().reset_index(name='count')

    # Pivot the table for plotting: ages are now the lines, total_score is x-axis
    _score_age_pivot = _score_age_distribution.pivot(index='total_score', columns='age', values='count').fillna(0)

    # Create the line plot with ages as separate lines
    _fig = px.line(_score_age_pivot, labels={'value': 'Count of Children', 'index': 'Total Test Score'})
    _fig.update_layout(
        title="Age-specific Distribution of Total Test Scores",
        xaxis_title="Total Test Score",
        yaxis_title="Count of Children",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )

    # Show the figure
    age_line_plot = _fig
    return age_line_plot,


@app.cell
def __(mo, plot5):
    mo.md(
        f"""
        ## What are the common traits (based on A1-A10 scores) among children diagnosed with ASD compared to those not diagnosed?  
        {mo.accordion({"Again !": plot5})}
        """
    )
    return


@app.cell
def __(mo, plot5):
    # add plot descrips here @line6
    q5 = mo.md(
        f"""
        {mo.as_html(plot5)}


        
        """
    )
    return q5,


@app.cell
def __(autism_df, mo, px):
    # Calculate the mean scores for each question by ASD diagnosis
    mean_scores = autism_df.groupby('ASD')[['A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score',
                                       'A6_Score', 'A7_Score', 'A8_Score', 'A9_Score', 'A10_Score']].mean().reset_index()

    # Prepare data for plotting
    melted_data = mean_scores.melt(id_vars='ASD', var_name='Question', value_name='Average Score')

    # Create a grouped bar chart
    _fig = px.bar(melted_data, x='Question', y='Average Score', color='ASD', barmode='group',
                 title='Common Traits Based on A1-A10 Scores Among ASD Diagnosed and Non-Diagnosed Children',
                 labels={'Question': 'Question (A1-A10)', 'Average Score': 'Average Score'},
                 category_orders={"jundice": ["yes", "no"], "ASD": ["YES", "NO"]},
                  color_discrete_sequence=px.colors.qualitative.T10,
                 )


    _fig.update_layout(
        xaxis_title='Questions (A1 to A10)',
        yaxis_title='Average Score',
        legend_title="ASD Diagnosis"
    )

    _config = {
        'responsive': True,
        'displayModeBar': False
    }
    # fig.show() replaced below to be able to be seen in app view
    plot5 = mo.ui.plotly(_fig, _config)
    return mean_scores, melted_data, plot5


@app.cell
def __(mo, score_probs_plot):
    mo.md(
        f"""
        ## What is the probability of each Question being answered "Yes" among individuals diagnosed with ASD?

        {mo.accordion({"Last time!": score_probs_plot})}
        """
    )
    return


@app.cell
def __(mo, score_probs_plot):
    # add plot descrips here @line6
    q6 = mo.md(
        f"""
        {mo.as_html(score_probs_plot)}


        
        """
    )
    return q6,


@app.cell
def __(autism_df, go):
    # Filter data for individuals diagnosed with ASD
    _asd_yes = autism_df[autism_df["ASD"] == "YES"]

    # Calculate the percentage of 'Yes' responses for each question among ASD diagnosed individuals
    _question_columns = [col for col in autism_df.columns if "Score" in col]
    _percentages = [(_asd_yes[col].sum() / len(_asd_yes)) * 100 for col in _question_columns]

    # Format percentages to two significant figures
    _formatted_percentages = ["{:.2f}%".format(p) for p in _percentages]

    # Create a bar chart to visualize this data
    _fig_bar = go.Figure(
        [
            go.Bar(
                x=_question_columns,
                y=_percentages,
                text=_formatted_percentages,
                textposition="auto",
            )
        ]
    )
    _fig_bar.update_layout(
        title_text='Percentage of "Yes" Responses for Each Question Among ASD Diagnosed Individuals',
        xaxis_title="Question",
        yaxis_title="Percentage of 'Yes' Responses (%)",
        yaxis=dict(range=[0, 100]),
    )

    # Show the figure
    score_probs_plot = _fig_bar
    return score_probs_plot,


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
