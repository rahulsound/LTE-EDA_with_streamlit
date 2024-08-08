import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import plotly.express as px

#from Telecom_EDA import *
st.set_page_config(page_title='Telecom EDA ',layout='wide')
import os
import sys

def run_sub_header(online=True):
    if online:    
        st.write('[ [A StartupFounder](https://rahulsound.streamlit.app/A_StartupFounder) | \
                [Consultancy](https://rahulsound.streamlit.app/Consultancy) | \
                [AI ML Projects](https://rahulsound.streamlit.app/AI_ML_Projects) | \
                [Research](https://rahulsound.streamlit.app/Research) | \
                [Patents](https://rahulsound.streamlit.app/Patents) |\
                [Skills](https://rahulsound.streamlit.app/Skills) ]')
    else:
        st.write('| [AIMLProjects](http://localhost:8501/AIMLProjects) | \
                [Expertise](http://localhost:8501/Expertise) | \
                [Explora](http://localhost:8501/Explora) | \
                [MLInTelecom](http://localhost:8501/MLInTelecom) | \
                [Patents](http://localhost:8501/Patents) | \
                [Research](http://localhost:8501/ResearchPapers) |\
                [Start-up](http://localhost:8501/Startup) ]')
        
def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in ('.csv','.xlsx'):
        return ext
    else:
        return False


def run_additional_eda(df):
    num_cols = df.columns
    st.markdown('''
                ---
                ### :violet[Explore Data:]
                '''
                )


    col1, col2 = st.columns(2)
    with col1:
        cat_selection = st.selectbox("Select criterion to plot fig1:",num_cols)
        num_selection1 = st.selectbox("Select feature 1 to plot fig1:", num_cols)
        num_selection2 = st.selectbox("Select feature 2 to plot fig1:", num_cols)
        fig = px.scatter(data_frame=df, x=num_selection1, y=num_selection2, color=cat_selection)
        st.plotly_chart(fig) 
    with col2:
        cat_selectiona = st.selectbox("Select criterion to plot fig2:",num_cols)
        num_selectiona1 = st.selectbox("Select feature 1 to plot fig2:", num_cols)
        num_selectiona2 = st.selectbox("Select feature 2 to plot fig2:", num_cols)
        figa = px.scatter(data_frame=df, x=num_selectiona1, y=num_selectiona2, color=cat_selectiona)
        st.plotly_chart(figa) 


@st.fragment()
def run_profiler():
    st.subheader('Profiler')
    cols = st.columns(1)
    select = cols[0].toggle("Run Profiler")
    if select:
        choice = st.radio('Select data for Analysis', ('Reset', 'Illustration', 'Upload your own file'))

        if choice == 'Illustration':
            df = pd.DataFrame()
            df = pd.read_csv('site1.csv')
            st.write(df.head())
            st.title('Data Profiler is generating report::')
            #pr = ProfileReport(df, minimal=True)#explorative=True
            pr = ProfileReport(df, explorative=True,                                    
                                            correlations={
                                            "pearson": {"calculate": True},
                                            "spearman": {"calculate": True},
                                            "kendall": {"calculate": False},
                                            "phi_k": {"calculate": False},
                                        })#explorative=True
            pr.config.plot.scatter_threshold = 25000
            st_profile_report(pr)
            df.to_csv('illus.csv')
            st.session_state['count']+=1
            st.session_state['df'] = df
            st.session_state['last_action'] = 'illus'

            return df
        
        elif choice =='Upload your own file':
            df = pd.DataFrame()
            uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
            if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                st.write(df.head())
                st.title('Data Profiler is generating report::')
                #pr = ProfileReport(df, minimal=True)#explorative=True
                pr = ProfileReport(df, explorative=True,                                    
                                                correlations={
                                                "pearson": {"calculate": True},
                                                "spearman": {"calculate": True},
                                                "kendall": {"calculate": False},
                                                "phi_k": {"calculate": False},
                                            })#explorative=True
                pr.config.plot.scatter_threshold = 25000
                st_profile_report(pr)
                df.to_csv('upload.csv')
                st.session_state['count']+=1
                st.session_state['df'] = df
                st.session_state['upload'] = 1
                st.session_state['last_action'] = 'upload'
                return df   
        else:
            st.session_state['count'] = 0
            st.session_state['df'] = None
            st.session_state['upload'] = 0
            st.session_state['last_action'] = None

@st.fragment()
def run_eda():
    st.subheader('EDA')
    # st.write('Last Action:', st.session_state['last_action'])
    cols = st.columns(1)
    select = cols[0].toggle("Explore")
    if select:
        choice = st.radio('Select data for EDA', ('Illustration file', 'Uploaded file'))
        if choice == 'Illustration file':  
            st.subheader('Illustration file:')
            if os.path.isfile('illus.csv'):
                df1 = pd.read_csv('illus.csv')
                run_additional_eda(df1)
            else:
                st.write("Please run 'Profile' on demo file first... ")
        elif choice == 'Uploaded file':
            st.subheader('Uploaded file:')
            if os.path.isfile('upload.csv'):
                df1 = pd.read_csv('upload.csv')
                run_additional_eda(df1)
            else:
                st.write('Please upload your file first for Profiling...')
        else:
            st.subheader('Empty')

####################################################################################
#Main Execution::
####################################################################################
st.subheader(":blue[Rahul Soundrarajan]", anchor='#about')
st.markdown('''
###### [LinkedIn](https://www.linkedin.com/in/rahul-soundrarajan/) | [Medium](https://medium.com/@rahulsound) | [Contact](mailto:rahulsound@gmail.com)
                
            ''')
run_sub_header()
st.header(":blue[Exploratory Analysis of Telecom dataset made easy with a few lines of code]", anchor='#TelecomDataPlay')
st.markdown('''
### :blue[Bring your own data and play with it right here! ]   
---        
##### For illustrative purposes, I have used openly available Telecom dataset to show the power of libraries such as [**pandas-profiling**](https://pypi.org/project/pandas-profiling/)   
            ''')
# st.markdown(''' The [**pandas**](https://en.wikipedia.org/wiki/Pandas_(software)) Python library offers data structures and operations for manipulating numerical tables and time series. 
# It makes it an ideal library to process Telecom datasets (especially PMs and KPIs) that are in tabular format.''')

st.write("")


col1, col2 = st.columns(2)
with col1:
    st.write(''' 
                ##### :violet[**4G LTE** dataset]:   
                -   **Published**: 1 April 2020 | Version 1 | DOI: 10.17632/bfkdfy6x95.1 Contributors: Agbotiname Imoize , Kehinde Orolu , Prof. Aderemi Aaron-Anthony Atayero
                -   **Title**: "Data for Analysis of Key Performance Indicators of a 4G LTE Network Based on Experimental Data Obtained from a Densely Populated Smart City".   
                -   **Source**: https://data.mendeley.com/datasets/bfkdfy6x95/1 
                -   **Citation**: Imoize, Agbotiname; Orolu, Kehinde; Atayero, Prof. Aderemi Aaron-Anthony  (2020), “Data for: Analysis of Key Performance Indicators of a 4G LTE Network Based on Experimental Data Obtained from a Densely Populated Smart City”, Mendeley Data, V1, doi: 10.17632/bfkdfy6x95.1                                
                -   **Link to the research paper**: [[here]](https://pdf.sciencedirectassets.com/311593/1-s2.0-S2352340922X00036/1-s2.0-S2352340922004425/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLWVhc3QtMSJHMEUCIA%2FM5UupOQp9mFyX%2Bm09HVO30rZGEUytCaHJG0mIOYAhAiEAti8yVy9QPPvpGYKvjX%2Flz7LGae7G4iCkdV%2FEiH8xPNwqswUILhAFGgwwNTkwMDM1NDY4NjUiDIqNMzR7%2F8zT90NCZiqQBVAQWbzXpXN0h4nl8kB318bFof8j1QyzMRjpt6XMaMbPQiaHk48wL5Fx4OKxabiwvIBrDdF7P%2BYXdCf6Mc3PvP4fC81whFMc9zFu4MuF3OyKw%2FikcvHadPX9XeMuCeauLLbJd7iTQKJlCPbFqUKwZUsjR6Mcuo6%2BCyKLryrqcMtGjYqSHYU0Ig%2FfYYg70fM1umvG2pNuqPGxNKbwwkYzE3MYgKO1BHENXngumsNRqC6HyMSsZHLxz99UNkScF4aoLfW0ImAPmKog9DE4YXB45zMWDJdRHk4zJVpf%2B%2Bn5URl7hsX1H3o0G8yx4KGUQdgm4WkQNBidI3DizZtNp73wHREhbSKoHNqavNuT0hrg9Y0TMnQS1jhr5osQkfcJjWfGY3SqOoAzwSzu5Jhq%2FHICW66I4KwlxVfTWXVn8gr%2B6DrRZNTu9jm7IrGSCLOXKyoAKoFPwOUgvQRkwGprgSWZUZHODdagYOaksm7uUIitUyrS8TybramtFtDcBjrdRsO8w0smC%2FQ6GXC3OXpbgbTiClMdujRQYSmOLDsoz4ZxQDMyhFWx4k8mlg28XuRlv0e%2FjqYEKst4AhXv5GP7xpu3h%2BbuMdBKtRpACdK06atMZPrcqxjA7wjSBFKOYghSyJFgZu3o05esh%2ByjQQNTBH28trsLRvsZv1jaC9MCKXiU0r40CqD%2FOY4DTmLNdvGYmdF4zB%2BP9sK16NLWFq4URAtj8Iq3U1ls5ZFi5hlsT8LnG2UGPXDxyLPnPvklgHBrOnpo3hGuvZ3eyNPnRL9RBk7tXRV1dBJHxihVKJ37%2FtzVccttRPAwd7hOabmcyHO%2F3CAveLxKrGdH5U3UZTC5IyN18N%2FF3eV9hAyMGtx8opxTjDTbMIXy0rUGOrEBruKqm%2B1r9U9pjBEdWpeSQbfv5ClYqD%2Fi2MBYdtmghJiOufFBHGp3GXgfpcFheCEMiNKHyDUyMrjEPx3whHo%2BvY5R%2FYyVwDl52MZMr65PaBGef87Kz66T4T7W6bXnDrA2NIj7odfOweOMfdjiHY7JDFqjagur2xgVQRLaFjzmZGCQpiK0kI5WNflIujlVFZKZYHmXCezBsxGLDm1KPAhBRrVPoJYjo6Y7OSNHJ15VMZ4r&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240808T132505Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY7RNGVBHL%2F20240808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=a8231815461b98f249b845999bfeecf0904417a96949a5616ac983c311dfd946&hash=751aafd369f42d801891a4943e0ae0823d5bc73c5e8b284a462facaa37b920f4&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2352340922004425&tid=spdf-beae4ed1-cda2-4bc7-ae47-6cb17723a2a9&sid=ec108a4c1f3d394ca648e659336fa0099bf0gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=090b5b05040304525b&rr=8affd4904f1fb28e&cc=in)
             ''')
with col2:
    st.write(''' 
                ##### :violet[Libraries & Repos]:   
                -   pandas-profiling: https://github.com/ydataai/ydata-profiling
                -   How to use pandas-profiling with Streamlit: https://github.com/dataprofessor/eda-app 
             ''')
    st.code('''
            #imports
            import numpy as np
            import pandas as pd
            from ydata_profiling import ProfileReport

            #Create dummy data
            df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
            
            #To generate the standard profiling report, merely run:
            profile = ProfileReport(df, title="Profiling Report")
            ''', language='python')
   
if 'count' not in st.session_state:
    st.session_state['count'] = 0
    st.session_state['df'] = None
    st.session_state['upload'] = 0
    st.session_state['last_action'] = None

st.divider()
st.subheader('How to use this page:')
st.markdown('''
            -   Toggle the [**Run Profiler**] button in the [**Profile Tab**] below to explore the output of pandas-profiling on the above dataset.
            -   Toogle the [**Explore**] button in the [**EDA Tab**] to visualize interesting correlation plots.
            -   If you happen to have a clean 'csv' file, use the "Upload your own file" radio button under [**Profile Tab**].   
            ''')
st.write(':red[Note1:] The profiler needs to crunch data and generate reports, it might take ~30s depending on the size of the data.')
st.write(':red[Note2:] The data provided in the above link had to be cleaned before feeding it to pandas-profiling')
            
profile_tab, eda_tab  = st.tabs(["Profile Tab", "EDA Tab"])
with profile_tab:
    run_profiler()
st.divider()
with eda_tab:
    run_eda()
st.divider()
#st.write('Count = ', st.session_state['count'])