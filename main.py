import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

# <------ Set layout of web ---------->
st.set_page_config(layout="wide")

st.title("Data Dashboard")
st.header(f"Platforms")

# <------ Authorization header for APIs ---------->
headers = {
    'Authorization': 
    'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'
    }
    
# @st.cache_resource(ttl=1800)
# def dataload():
    

    
   
#     url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=30"
#     response = requests.request("GET", url, headers=headers)
#     data30= json.loads(response.text)
#     print("\n\n\nStatus code::::",response.status_code)

#     # while response.status_code == 502:
#     #     response = requests.request("GET", url, headers=headers)
#     #     print("\n\n\nStatus code::::",response.status_code)
#     #     data30= json.loads(response.text)
        
#     print("Data 30 days: ",data30['data'])
    
    
#     url = "http://api.aicarz.com/api/v1/dev/data-dashboard"
#     response = requests.request("GET", url, headers=headers)
#     data_lifetime= json.loads(response.text)
#     print("\n\n\nStatus code::::",response.status_code)

#     # while response.status_code == 502:
#     #     response = requests.request("GET", url, headers=headers)
#     #     print("\n\n\nStatus code::::",response.status_code)
#     #     data_lifetime= json.loads(response.text)
        
#     print("Data lifetime: ",data_lifetime['data'])
    
#     return data1['data'], data7['data'], data15['data'], data30['data'], data_lifetime['data']





# <------  Here I call dataload function and store all data in variables  ---------->
# data1, data7, data15, data30, data_lifetime= dataload()




@st.cache_resource(ttl=1800)
def last24hours():
    
        # <------ Call API for last 24 hours data ---------->
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=1"
    response = requests.request("GET", url, headers=headers)
    data1= json.loads(response.text)['data']
    print("\n\n\nStatus code::::",response.status_code)

    # <------ If API server give 502 error  ---------->
    while response.status_code == 502:
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)
        data1= json.loads(response.text)
        
    print("Data 1 day: ",data1)
    
    
    # <------  Store active data count into variables for last 24 hours  ---------->
    total_active_24 = [data1["count"]["activeFacebook"], data1["count"]["activeHeyCars"], data1["count"]["activeAutoTrader"], data1["count"]["activeGumtree"],data1["count"]["activeMotors"]]

    # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
    total_nonactive_24 = [data1["checkerActivity"]["deactivatedCountFacebook"], data1["checkerActivity"]["deactivatedCountHeyCars"], data1["checkerActivity"]["deactivatedCountAutoTrader"], data1["checkerActivity"]["deactivatedCountGumtree"], data1["checkerActivity"]["deactivatedCountMotors"]]

    # <------  Store all count data into variables for 24 hours  ---------->
    total_count_24 = [data1["count"]["facebook"], data1["count"]["heyCars"], data1["count"]["autoTrader"], data1["count"]["gumtree"], data1["count"]["motors"]]

    last_24_hours= [total_active_24, total_nonactive_24, total_count_24]
    
    return last_24_hours


@st.cache_resource(ttl=1800)
def last7days():
    
    # <------ Call API for last 7 days data ---------->
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=7"
    response = requests.request("GET", url, headers=headers)
    data7= json.loads(response.text)['data']
    print("\n\n\nStatus code::::",response.status_code)

    # <------ If API server give 502 error  ---------->
    while response.status_code == 502:
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)
        data1= json.loads(response.text)
        
    print("Data 7 day: ",data7)
    
    # <------  Store deactive data into variables which deactivated in last 7 days  ---------->
    total_active_7 = [data7["count"]["activeFacebook"], data7["count"]["activeHeyCars"], data7["count"]["activeAutoTrader"], data7["count"]["activeGumtree"], data7["count"]["activeMotors"]] 
 
     # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
    total_nonactive_7 = [data7["checkerActivity"]["deactivatedCountFacebook"], data7["checkerActivity"]["deactivatedCountHeyCars"], data7["checkerActivity"]["deactivatedCountAutoTrader"], data7["checkerActivity"]["deactivatedCountGumtree"], data7["checkerActivity"]["deactivatedCountMotors"]]

    # <------  Store active data into variables for last 7 days  ---------->
    total_count_7 = [data7["count"]["facebook"], data7["count"]["heyCars"], data7["count"]["autoTrader"], data7["count"]["gumtree"], data7["count"]["motors"]]

    last_7_hours= [total_active_7, total_nonactive_7, total_count_7]
    
    return last_7_hours


@st.cache_resource(ttl=1800)
def last15days():
    
    # <------ Call API for last 15 days data ---------->
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
    response = requests.request("GET", url, headers=headers)
    data15= json.loads(response.text)['data']
    print("\n\n\nStatus code::::",response.status_code)

    # <------ If API server give 502 error  ---------->
    while response.status_code == 502:
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)
        data15= json.loads(response.text)
        
    print("Data 15 days: ",data15)
    
    # <------  Store active data into variables for last 15 days  ---------->
    total_active_15 = [data15["count"]["activeFacebook"],data15["count"]["activeHeyCars"],data15["count"]["activeAutoTrader"],data15["count"]["activeGumtree"],data15["count"]["activeMotors"]]

    # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
    total_nonactive_15 = [data15["checkerActivity"]["deactivatedCountFacebook"], data15["checkerActivity"]["deactivatedCountHeyCars"], data15["checkerActivity"]["deactivatedCountAutoTrader"], data15["checkerActivity"]["deactivatedCountGumtree"], data15["checkerActivity"]["deactivatedCountMotors"]]

    # <------  Store all count data into variables for 24 hours  ---------->
    total_count_15 = [data15["count"]["facebook"], data15["count"]["heyCars"], data15["count"]["autoTrader"], data15["count"]["gumtree"], data15["count"]["motors"]]

    last_15= [total_active_15, total_nonactive_15, total_count_15]
    
    return last_15



@st.cache_resource(ttl=1800)
def last30days():

    # <------ Call API for last 30 days data ---------->
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=30"
    response = requests.request("GET", url, headers=headers)
    data30= json.loads(response.text)['data']
    print("\n\n\nStatus code::::",response.status_code)

    # <------ If API server give 502 error  ---------->
    while response.status_code == 502:
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)
        data15= json.loads(response.text)
        
    print("Data 30 days: ",data30)
    
    # <------  Store active data into variables for last 15 days  ---------->
    total_active_30 = [data30["count"]["activeFacebook"],data30["count"]["activeHeyCars"],data30["count"]["activeAutoTrader"],data30["count"]["activeGumtree"],data30["count"]["activeMotors"]]

    # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
    total_nonactive_30 = [data30["checkerActivity"]["deactivatedCountFacebook"], data30["checkerActivity"]["deactivatedCountHeyCars"], data30["checkerActivity"]["deactivatedCountAutoTrader"], data30["checkerActivity"]["deactivatedCountGumtree"], data30["checkerActivity"]["deactivatedCountMotors"]]

    # <------  Store all count data into variables for 24 hours  ---------->
    total_count_30 = [data30["count"]["facebook"], data30["count"]["heyCars"], data30["count"]["autoTrader"], data30["count"]["gumtree"], data30["count"]["motors"]]

    last_30= [total_active_30, total_nonactive_30, total_count_30]
    
    return last_30



@st.cache_resource(ttl=1800)
def lifetime():

    # <------ Call API for last lifetime data ---------->
    url = "http://api.aicarz.com/api/v1/dev/data-dashboard"
    response = requests.request("GET", url, headers=headers)
    data_lifetime= json.loads(response.text)['data']
    print("\n\n\nStatus code::::",response.status_code)

    # <------ If API server give 502 error  ---------->
    while response.status_code == 502:
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)
        data15= json.loads(response.text)
        
    print("Data 30 days: ",data_lifetime)
    
    # <------  Store active data into variables for last 15 days  ---------->
    total_active_lifetime = [data_lifetime["count"]["activeFacebook"],data_lifetime["count"]["activeHeyCars"],data_lifetime["count"]["activeAutoTrader"],data_lifetime["count"]["activeGumtree"],data_lifetime["count"]["activeMotors"]]

    # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
    total_nonactive_lifetime = [data_lifetime["checkerActivity"]["deactivatedCountFacebook"], data_lifetime["checkerActivity"]["deactivatedCountHeyCars"], data_lifetime["checkerActivity"]["deactivatedCountAutoTrader"], data_lifetime["checkerActivity"]["deactivatedCountGumtree"], data_lifetime["checkerActivity"]["deactivatedCountMotors"]]

    # <------  Store all count data into variables for 24 hours  ---------->
    total_count_lifetime = [data_lifetime["count"]["facebook"], data_lifetime["count"]["heyCars"], data_lifetime["count"]["autoTrader"], data_lifetime["count"]["gumtree"], data_lifetime["count"]["motors"]]

    last_lifetime= [total_active_lifetime, total_nonactive_lifetime, total_count_lifetime]
    
    return last_lifetime



# <------ Dropdown to select the data set ---------->
dataset_name = st.selectbox('Select a Dataset', ['Last 24 Hours','Lifetime', 'Last 30 days','Last 15 days', 'Last 7 days', 'Last 24 Hours'])


if dataset_name == 'Last 24 Hours':
    _24hours= last24hours()
    data_active = {'Last 24 Hours': _24hours[0]}
    data_nonactive = {'Last 24 Hours': _24hours[1]}
    data_total = {'Last 24 Hours': _24hours[2]}
    
elif dataset_name == 'Last 7 days':
    last7= last7days()
    data_active = {'Last 7 days': last7[0]}
    data_nonactive = {'Last 7 days': last7[1]}
    data_total = {'Last 7 days': last7[2]}
    
elif dataset_name == 'Last 15 days':
    last15= last15days()
    data_active = {'Last 15 days': last15[0]}
    data_nonactive = {'Last 15 days': last15[1]}
    data_total = {'Last 15 days': last15[2]}

elif dataset_name == 'Last 30 days':
    last30= last30days()
    data_active = {'Last 30 days': last30[0]}
    data_nonactive = {'Last 30 days': last30[1]}
    data_total = {'Last 30 days': last30[2]}
    
else:
    lifetime_= lifetime()
    data_active = {'Lifetime': lifetime_[0]}
    data_nonactive = {'Lifetime': lifetime_[1]}
    data_total = {'Lifetime': lifetime_[2]}
    
    
# <------ divide layout into three columns ---------->
left, center, right = st.columns(3)   

# <------ Active data graph ↓ ---------->
with left:   
    st.subheader(f"Active:")
    
    # <------ Custom color palette ---------->
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#BB33FF']

    # <------  this function convert % into float % if persentage is less then 1 ---------->
    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    
    
    # <------  Use try catch if values of all data is 0 then it display nothing instead of error ---------->
    try:   
    # <------  Create a pie chart for the selected data set -------->
        fig1, ax1 = plt.subplots()
        ax1.pie(data_active[dataset_name], 
                colors=colors, 
                autopct=custom_autopct, 
                pctdistance=0.85,
                explode=(0, 0, 0, 0, 0),  # Exploding the first slice
                counterclock=False
                )

        # <------  Draw a circle at the center to make it look like a donut -------->
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # <------  Add a legend (legend means colors with its lables) -------->
        plt.legend(["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"], loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        # <------  To display donut graph -------->
        st.pyplot(fig1) 
    except:
        pass
    
    # <------  To display actual numbers of records -------->
    st.markdown(f"Total number of active data for {dataset_name} on *Autotraders* is **{data_active[dataset_name][2]}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Gumtree* is **{data_active[dataset_name][3]}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Facebook* is **{data_active[dataset_name][0]}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Moters* is **{data_active[dataset_name][4]}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Heycars* is **{data_active[dataset_name][1]}**.")
    st.markdown(f"Total number of active data for {dataset_name} on all *Platforms* is **{data_active[dataset_name][1] + data_active[dataset_name][4] + data_active[dataset_name][0]+data_active[dataset_name][3] + data_active[dataset_name][2]}**.")
    # st.markdown("-------------------------------------------------------------------------------")




# <------ deactive data graph ↓ ---------->
with center:
    st.subheader(f"Inactive:")
    
    # <------ Custom color palette ---------->
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#BB33FF']

    # <------  this function convert % into float % if persentage is less then 1 ---------->
    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    
     # <------  Use try catch if values of all data is 0 then it display nothing instead of error ---------->
    try:   
        # <------  Create a pie chart for the selected data set -------->
        fig1, ax1 = plt.subplots()
        ax1.pie(data_nonactive[dataset_name], 
                colors=colors, 
                autopct=custom_autopct, 
                pctdistance=0.85,
                explode=(0, 0, 0, 0, 0),  # Exploding the first slice
                counterclock=False
                )

        # <------  Draw a circle at the center to make it look like a donut -------->
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig1.gca().add_artist(centre_circle)


        # <------  Add a legend (legend means colors with its lables) -------->
        
        plt.legend(["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"], loc="lower left", bbox_to_anchor=(1, 0, 1, 1))
        
        # <------  To display donut graph -------->
        st.pyplot(fig1)
    except:
        pass
    
    # <------  To display actual numbers of records -------->
    st.markdown(f"Total number of non-active data for {dataset_name} on *Autotraders* is **{data_nonactive[dataset_name][2]}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Gumtree* is **{data_nonactive[dataset_name][3]}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Facebook* is **{data_nonactive[dataset_name][0]}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Moters* is **{data_nonactive[dataset_name][4]}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Heycars* is **{data_nonactive[dataset_name][1]}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on all *Platforms* is **{data_nonactive[dataset_name][1] + data_nonactive[dataset_name][4] + data_nonactive[dataset_name][0] + data_nonactive[dataset_name][3] + data_nonactive[dataset_name][2]}**.")
    # st.markdown("-------------------------------------------------------------------------------") 




# <------ Total data graph ↓ ---------->
with right:
    st.subheader(f"Total:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#BB33FF']   


    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''

    try:
        # Create a pie chart for the selected data set
        fig1, ax1 = plt.subplots()
        ax1.pie(data_total[dataset_name], 
                colors=colors, 
                # labels=df.index, 
                autopct=custom_autopct, 
                # startangle= 90,
                pctdistance=0.85,
                explode=(0, 0, 0, 0, 0),  # Exploding the first slice
                # shadow=True
                
                counterclock=False
                )

        # Draw a circle at the center to make it look like a donut
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig1.gca().add_artist(centre_circle)

        # ax1.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle

        # Add a legend
        plt.legend(["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"], loc="lower left", bbox_to_anchor=(1, 0, 1, 1))
        # Display the pie chart
        st.pyplot(fig1)
    except:
        pass
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Autotraders* is **{data_total[dataset_name][2]}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Gumtree* is **{data_total[dataset_name][3]}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Facebook* is **{data_total[dataset_name][0]}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Moters* is **{data_total[dataset_name][4]}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Heycars* is **{data_total[dataset_name][1]}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on all *Platforms* is **{data_total[dataset_name][1] + data_total[dataset_name][4] + data_total[dataset_name][0] + data_total[dataset_name][3] + data_total[dataset_name][2]}**.")


# data = {
#     'Last 24 Hours': [total_active_autotrader_24,total_nonactive_autotrader_24],
#     'Last 7 days': [total_active_autotrader_7, total_nonactive_autotrader_7],
#     'Last 15 days': [total_active_autotrader_15, total_nonactive_autotrader_15],
#     'Last 30 days': [total_active_autotrader_30, total_nonactive_autotrader_30],
#     'Lifetime': [total_active_autotrader, total_nonactive_autotrader]
# }
# df = pd.DataFrame(data, index=["Active", "Non-Active"])


# left,center, right = st.columns(3)   
# with left:   
#     st.subheader(f"Autotraders:")
#     # Custom color palette
#     colors = ['#ff9999','#66b3ff']

#     def custom_autopct(pct):
#         return ('%1.1f%%' % pct) if pct >= 1 else ''
#     # Create a pie chart for the selected data set
#     try:   
#         fig1, ax1 = plt.subplots()
#         ax1.pie(df[dataset_name], 
#                 colors=colors, 
#                 # labels=df.index, 
#                 autopct=custom_autopct, 
#                 # startangle= 90,
#                 pctdistance=0.85,
#                 explode=(0, 0),  # Exploding the first slice
#                 # shadow=True
#                 counterclock=False
#                 )

#         # Draw a circle at the center to make it look like a donut
#         centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#         fig1.gca().add_artist(centre_circle)

#         # Add a legend
#         plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

#         st.pyplot(fig1) 
#     except:
#         pass

#     st.markdown(f"Total number of active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Active']}**.")
#     st.markdown(f"Total number of non-active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Non-Active']}**.")
#     st.markdown(f"Total number of data for {dataset_name} on all *Autotraders* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")


# data = {
#     'Last 24 Hours': [total_active_gumtree_24,total_nonactive_gumtree_24],
#     'Last 7 days': [total_active_gumtree_7, total_nonactive_gumtree_7],
#     'Last 15 days': [total_active_gumtree_15, total_nonactive_gumtree_15],
#     'Last 30 days': [total_active_gumtree_30, total_nonactive_gumtree_30],
#     'Lifetime': [total_active_gumtree, total_nonactive_gumtree]
# }
# df = pd.DataFrame(data, index=["Active", "Non-Active"])


# with center:   
#     st.subheader(f"Gumtree:")
#     # Custom color palette
#     colors = ['#ff9999','#66b3ff']

#     def custom_autopct(pct):
#         return ('%1.1f%%' % pct) if pct >= 1 else ''
#     # Create a pie chart for the selected data set
#     try:   
#         fig1, ax1 = plt.subplots()
#         ax1.pie(df[dataset_name], 
#                 colors=colors, 
#                 # labels=df.index, 
#                 autopct=custom_autopct, 
#                 # startangle= 90,
#                 pctdistance=0.85,
#                 explode=(0, 0),  # Exploding the first slice
#                 # shadow=True
#                 counterclock=False
#                 )

#         # Draw a circle at the center to make it look like a donut
#         centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#         fig1.gca().add_artist(centre_circle)

#         # Add a legend
#         plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

#         st.pyplot(fig1) 
#     except:
#         pass

#     st.markdown(f"Total number of active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Active']}**.")
#     st.markdown(f"Total number of non-active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Non-Active']}**.")
#     st.markdown(f"Total number of data for {dataset_name} on all *Gumtree* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    


# data = {
#     'Last 24 Hours': [total_active_facebook_24,total_nonactive_facebook_24],
#     'Last 7 days': [total_active_facebook_7, total_nonactive_facebook_7],
#     'Last 15 days': [total_active_facebook_15, total_nonactive_facebook_15],
#     'Last 30 days': [total_active_facebook_30, total_nonactive_facebook_30],
#     'Lifetime': [total_active_facebook, total_nonactive_facebook]
# }
# df = pd.DataFrame(data, index=["Active", "Non-Active"])


# with right:   
#     st.subheader(f"Facebook:")
#     # Custom color palette
#     colors = ['#ff9999','#66b3ff']

#     def custom_autopct(pct):
#         return ('%1.1f%%' % pct) if pct >= 1 else ''
#     # Create a pie chart for the selected data set
#     try:   
#         fig1, ax1 = plt.subplots()
#         ax1.pie(df[dataset_name], 
#                 colors=colors, 
#                 # labels=df.index, 
#                 autopct=custom_autopct, 
#                 # startangle= 90,
#                 pctdistance=0.85,
#                 explode=(0, 0),  # Exploding the first slice
#                 # shadow=True
#                 counterclock=False
#                 )

#         # Draw a circle at the center to make it look like a donut
#         centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#         fig1.gca().add_artist(centre_circle)

#         # Add a legend
#         plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

#         st.pyplot(fig1) 
#     except:
#         pass

#     st.markdown(f"Total number of active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Active']}**.")
#     st.markdown(f"Total number of non-active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Non-Active']}**.")
#     st.markdown(f"Total number of data for {dataset_name} on all *Facebook* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    

# data = {
#     'Last 24 Hours': [total_active_heycar_24,total_nonactive_heycar_24],
#     'Last 7 days': [total_active_heycar_7, total_nonactive_heycar_7],
#     'Last 15 days': [total_active_heycar_15, total_nonactive_heycar_15],
#     'Last 30 days': [total_active_heycar_30, total_nonactive_heycar_30],
#     'Lifetime': [total_active_heycar, total_nonactive_heycar]
# }
# df = pd.DataFrame(data, index=["Active", "Non-Active"])


# with left:   
#     st.subheader(f"Heycar:")
#     # Custom color palette
#     colors = ['#ff9999','#66b3ff']

#     def custom_autopct(pct):
#         return ('%1.1f%%' % pct) if pct >= 1 else ''
#     # Create a pie chart for the selected data set
#     try:   
#         fig1, ax1 = plt.subplots()
#         ax1.pie(df[dataset_name], 
#                 colors=colors, 
#                 # labels=df.index, 
#                 autopct=custom_autopct, 
#                 # startangle= 90,
#                 pctdistance=0.85,
#                 explode=(0, 0),  # Exploding the first slice
#                 # shadow=True
#                 counterclock=False
#                 )

#         # Draw a circle at the center to make it look like a donut
#         centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#         fig1.gca().add_artist(centre_circle)

#         # Add a legend
#         plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

#         st.pyplot(fig1) 
#     except:
#         pass

#     st.markdown(f"Total number of active data for {dataset_name} on *Heycar* is **{df[dataset_name]['Active']}**.")
#     st.markdown(f"Total number of non-active data for {dataset_name} on *Heycar* is **{df[dataset_name]['Non-Active']}**.")
#     st.markdown(f"Total number of data for {dataset_name} on all *Heycar* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    

# data = {
#     'Last 24 Hours': [total_active_motors_24,total_nonactive_motors_24],
#     'Last 7 days': [total_active_motors_7, total_nonactive_motors_7],
#     'Last 15 days': [total_active_motors_15, total_nonactive_motors_15],
#     'Last 30 days': [total_active_motors_30, total_nonactive_motors_30],
#     'Lifetime': [total_active_motors, total_nonactive_motors]
# }
# df = pd.DataFrame(data, index=["Active", "Non-Active"])

# with center:   
#     st.subheader(f"Motors:")
#     # Custom color palette
#     colors = ['#ff9999','#66b3ff']

#     def custom_autopct(pct):
#         return ('%1.1f%%' % pct) if pct >= 1 else ''
#     # Create a pie chart for the selected data set
#     try:   
#         fig1, ax1 = plt.subplots()
#         ax1.pie(df[dataset_name], 
#                 colors=colors, 
#                 # labels=df.index, 
#                 autopct=custom_autopct, 
#                 # startangle= 90,
#                 pctdistance=0.85,
#                 explode=(0, 0),  # Exploding the first slice
#                 # shadow=True
#                 counterclock=False
#                 )

#         # Draw a circle at the center to make it look like a donut
#         centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#         fig1.gca().add_artist(centre_circle)

#         # Add a legend
#         plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

#         st.pyplot(fig1) 
#     except:
#         pass

#     st.markdown(f"Total number of active data for {dataset_name} on *Motors* is **{df[dataset_name]['Active']}**.")
#     st.markdown(f"Total number of non-active data for {dataset_name} on *Motors* is **{df[dataset_name]['Non-Active']}**.")
#     st.markdown(f"Total number of data for {dataset_name} on all *Motors* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    

    # st.markdown("-------------------------------------------------------------------------------")
    # Sample data
    # Sample data
# st.markdown("**________________________________________________________________________________________________________________________________________________________________________________**")




# st.header("Data Stats")
# st.markdown("-------------------------------------------------------------------------------")


# left,centerleft,centerright, right = st.columns(4)   
# connection_string = "mongodb+srv://dbuser123:VkzPhWfVCq4mr9M@cluster0.1gvhuro.mongodb.net/?retryWrites=true&w=majority"
# mongodbConn = pymongo.MongoClient(connection_string)
# carzdb = mongodbConn["aicarsStagingdb"]
# collection1 = carzdb["dataNotProcesseed"]
# collection2 = carzdb["FBdataNotProcesseed"]


# unique_car_buylinks = collection1.distinct("carBuyLink")
# unique_car_buylinks2 = collection2.distinct("carBuyLink")

# with left:
#     st.markdown(f"Data onboard today: **{format(collection.count_documents({'createdOn': {'$gte': twenty_four_hours_ago},}), ',')}**")
#     # st.subheader(f"Last day data onboard: {753256}")
#     st.markdown(f"No. of Data failure: **{format(len(unique_car_buylinks)+len(unique_car_buylinks2), ',')}**")
#     # st.subheader(f"No. of data failure: {753256}")
#     st.markdown("-------------------------------------------------------------------------------")

#     # Query to find the minimum price value where isActive is true
#     min_result = list(collection.find({'isActive': True, 'price': {'$ne': None}}).sort('price', 1).limit(1))
#     min_value = format(min_result[0]['price'], ",") if min_result else None


#     # Query to find the maximum price value where isActive is true
#     max_result = list(collection.find({'isActive': True, 'price': {'$ne': None}}).sort('price', -1).limit(1))
#     max_value = format(max_result[0]['price'], ",") if max_result else None

#     print(f"Minimum value: {min_value}")
#     print(f"Maximum value: {max_value}")

#     # Displaying in Streamlit
#     st.markdown(f"Max price in active data: **{max_value}£**")
#     st.markdown(f"Min price in active data: **{min_value}£**")
#     st.markdown("-------------------------------------------------------------------------------")

# # Adjusting queries to exclude documents where 'engineSizeInLiter' is None
# # Query to find the minimum engine size in liters where isActive is true and engineSizeInLiter is not None
# min_result = list(collection.find({'isActive': True, 'engineSizeInLiter': {'$ne': None}}).sort('engineSizeInLiter', 1).limit(1))
# min_value = min_result[0]['engineSizeInLiter'] if min_result else None

# # Query to find the maximum engine size in liters where isActive is true and engineSizeInLiter is not None
# max_result = list(collection.find({'isActive': True, 'engineSizeInLiter': {'$ne': None}}).sort('engineSizeInLiter', -1).limit(1))
# max_value = max_result[0]['engineSizeInLiter'] if max_result else None

# with centerleft:
#     # Displaying in Streamlit
#     if max_value is not None:
#         st.markdown(f"Max engine size in liter in active data: **{max_value}**")

#     if min_value is not None:
#         st.markdown(f"Min engine size in liter in active data: **{min_value}**")
#     st.markdown("-------------------------------------------------------------------------------")



#     # Query to find the minimum makeYear where isActive is true and makeYear is not None
#     min_result = list(collection.find({'isActive': True, 'year': {'$ne': None}}).sort('year', 1).limit(1))
#     min_value = min_result[0]['year'] if min_result else None

#     # Query to find the maximum makeYear where isActive is true and makeYear is not None
#     max_result = list(collection.find({'isActive': True, 'year': {'$ne': None}}).sort('year', -1).limit(1))
#     max_value = max_result[0]['year'] if max_result else None

#     # Displaying in Streamlit

#     st.markdown(f"Max year in active data: **{max_value}**")

#     st.markdown(f"Min year in active data: **{min_value}**")
#     st.markdown("-------------------------------------------------------------------------------")

# with centerright:

#     # Query to find the minimum mileageInMiles where isActive is true and mileageInMiles is not None
#     min_result = list(collection.find({'isActive': True, 'mileageInMiles': {'$ne': None}}).sort('mileageInMiles', 1).limit(1))
#     min_value = format(min_result[0]['mileageInMiles'], ',') if min_result else None

#     # Query to find the maximum mileageInMiles where isActive is true and mileageInMiles is not None
#     max_result = list(collection.find({'isActive': True, 'mileageInMiles': {'$ne': None}}).sort('mileageInMiles', -1).limit(1))
#     max_value = format(max_result[0]['mileageInMiles'], ',') if max_result else None

#     # Displaying in Streamlit
#     st.markdown(f"Max mileage in active data: **{max_value}** miles")
#     st.markdown(f"Min mileage in active data: **{min_value}** miles")



#     st.markdown("-------------------------------------------------------------------------------")
#     # Aggregation pipeline to count unique makes where isActive is True
#     pipeline = [
#         {"$match": {"isActive": True}},  # Filter for isActive being True
#         {"$group": {"_id": "$make"}},  # Group by the 'make' field
#         {"$group": {"_id": None, "uniqueCount": {"$sum": 1}}}  # Count unique makes
#     ]

#     unique_make_count_result = list(collection.aggregate(pipeline))

#     if unique_make_count_result:
#         unique_make_count = format(unique_make_count_result[0]['uniqueCount'], ',')
#     else:
#         unique_make_count = 0

#     # Displaying in Streamlit
#     st.markdown(f"Total number of unique active makes: **{unique_make_count}**")
#     # st.markdown("-------------------------------------------------------------------------------")

#     # Aggregation pipeline to count unique makes where isActive is True
#     pipeline = [
#         {"$match": {"isActive": True}},  # Filter for isActive being True
#         {"$group": {"_id": "$model"}},  # Group by the 'model' field
#         {"$group": {"_id": None, "uniqueCount": {"$sum": 1}}}  # Count unique makes
#     ]

#     unique_model_count_result = list(collection.aggregate(pipeline))

#     if unique_model_count_result:
#         unique_model_count = format(unique_model_count_result[0]['uniqueCount'], ',')
#     else:
#         unique_model_count = 0

#     # Displaying in Streamlit
#     st.markdown(f"Total number of unique active model: **{unique_model_count}**")
#     st.markdown("-------------------------------------------------------------------------------")

# with right:


#     # Aggregation pipeline to find the most frequent make where isActive is True
#     pipeline = [
#         {"$match": {"isActive": True}},  # Filter to include only active makes
#         {"$group": {"_id": "$make", "count": {"$sum": 1}}},  # Group by make and count
#         {"$sort": {"count": -1}},  # Sort by count in descending order
#         {"$limit": 5}  # Limit to the top result
#     ]

#     most_frequent_make = list(collection.aggregate(pipeline))

#     if most_frequent_make:
#         make_name1 = most_frequent_make[0]['_id']
#         make_count1 = format(most_frequent_make[0]['count'], ',')
#     else:
#         make_name1 = "None"
#         make_count1 = 0

#     if most_frequent_make:
#         make_name2 = most_frequent_make[1]['_id']
#         make_count2 = format(most_frequent_make[1]['count'], ',')
#     else:
#         make_name2 = "None"
#         make_count2 = 0

#     if most_frequent_make:
#         make_name3 = most_frequent_make[2]['_id']
#         make_count3 = format(most_frequent_make[2]['count'], ',')
#     else:
#         make_name3 = "None"
#         make_count3 = 0

#     if most_frequent_make:
#         make_name4 = most_frequent_make[3]['_id']
#         make_count4 = format(most_frequent_make[3]['count'], ',')
#     else:
#         make_name4 = "None"
#         make_count4 = 0

#     if most_frequent_make:
#         make_name5 = most_frequent_make[4]['_id']
#         make_count5 = format(most_frequent_make[4]['count'], ',')
#     else:
#         make_name5 = "None"
#         make_count5 = 0

#     # Displaying in Streamlit
#     st.markdown(f"Active make on first position: **{make_name1}** (Count: **{make_count1}**)")
#     st.markdown(f"Active make on second position: **{make_name2}** (Count: **{make_count2}**)")
#     st.markdown(f"Active make on third position: **{make_name3}** (Count: **{make_count3}**)")
#     st.markdown(f"Active make on fourth position: **{make_name4}** (Count: **{make_count4}**)")
#     st.markdown(f"Active make on fifth position: **{make_name5}** (Count: **{make_count5}**)")

#     st.markdown("-------------------------------------------------------------------------------")

#     # Aggregation pipeline to find the most frequent fuelType where isActive is True
#     pipeline = [
#         {"$match": {"isActive": True}},  # Filter to include only active entries
#         {"$group": {"_id": "$fuelType", "count": {"$sum": 1}}},  # Group by fuelType and count
#         {"$sort": {"count": -1}},  # Sort by count in descending order
#         {"$limit": 1}  # Limit to the top result
#     ]

#     most_frequent_fuelType = list(collection.aggregate(pipeline))

#     if most_frequent_fuelType:
#         fuelType_name = most_frequent_fuelType[0]['_id']
#         fuelType_count = format(most_frequent_fuelType[0]['count'], ',')
#     else:
#         fuelType_name = "None"
#         fuelType_count = 0

#     # Displaying in Streamlit
#     st.markdown(f"Most frequent active fuel type: **{fuelType_name}** (Count: **{fuelType_count}**)")
#     st.markdown("-------------------------------------------------------------------------------")