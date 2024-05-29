import streamlit as st
import matplotlib.pyplot as plt
import requests
import json

# <------ Set layout of web ---------->
st.set_page_config(layout="wide")

try:
# load = st.button("Refresh")
    st.title("Data Dashboard")
    st.header(f"Platforms")

    # <------ Authorization header for APIs ---------->
    headers = {
        'Authorization': 
        'Bearer ya29.a0AfB_byASQo7lfEHHE4H6vXGd9MefYU0puZYAk3fkDyFcoJzE7Ra8Nzssy0TLcVuPyFRHvO_g_2h07UkZKtApTu51oJZb35PfvPN8UpPrvx4sU2yFzYclzdmmxBfRpymGYbziyD2JVLM9X2zEFSJabc2x157KKPGAQwaCgYKAbYSARISFQHGX2Mig9VTJWbXohan6iB9BtfcIg0169'
        }
        

# <------  Here I call dataload function and store all data in variables  ---------->
# @st.cache_resource(ttl=86400)

# if load==True :

    def last24hours():
        
            # <------ Call API for last 24 hours data ---------->
        url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=1"
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)

        # <------ If API server give 502 error  ---------->
        while response.status_code == 502:
            print('Again hitting API because API response is "502"')
            response = requests.request("GET", url, headers=headers)
            print("\n\n\nStatus code::::",response.status_code)
            # data1= json.loads(response.text)['data']
            
        data1= json.loads(response.text)['data']
        print("Data 1 day: ",data1)
        
        
        # <------  Store active data count into variables for last 24 hours  ---------->
        total_active_24 = [data1["count"]["activeFacebook"], data1["count"]["activeHeyCars"], data1["count"]["activeAutoTrader"], data1["count"]["activeGumtree"],data1["count"]["activeMotors"]]

        # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
        total_nonactive_24 = [data1["checkerActivity"]["deactivatedCountFacebook"], data1["checkerActivity"]["deactivatedCountHeyCars"], data1["checkerActivity"]["deactivatedCountAutoTrader"], data1["checkerActivity"]["deactivatedCountGumtree"], data1["checkerActivity"]["deactivatedCountMotors"]]

        # <------  Store all count data into variables for 24 hours  ---------->
        total_count_24 = [data1["count"]["facebook"], data1["count"]["heyCars"], data1["count"]["autoTrader"], data1["count"]["gumtree"], data1["count"]["motors"]]

        last_24_hours= [total_active_24, total_nonactive_24, total_count_24]
        
        return last_24_hours,data1


    # @st.cache_resource(ttl=86400)
    def last7days():
        
        # <------ Call API for last 7 days data ---------->
        url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=7"
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)

        # <------ If API server give 502 error  ---------->
        while response.status_code == 502:
            print('Again hitting API because API response is "502"')
            response = requests.request("GET", url, headers=headers)
            print("\n\n\nStatus code::::",response.status_code)
            # data7= json.loads(response.text)['data']
            
        data7= json.loads(response.text)['data']
        print("Data 7 day: ",data7)
        
        # <------  Store deactive data into variables which deactivated in last 7 days  ---------->
        total_active_7 = [data7["count"]["activeFacebook"], data7["count"]["activeHeyCars"], data7["count"]["activeAutoTrader"], data7["count"]["activeGumtree"], data7["count"]["activeMotors"]] 

        # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
        total_nonactive_7 = [data7["checkerActivity"]["deactivatedCountFacebook"], data7["checkerActivity"]["deactivatedCountHeyCars"], data7["checkerActivity"]["deactivatedCountAutoTrader"], data7["checkerActivity"]["deactivatedCountGumtree"], data7["checkerActivity"]["deactivatedCountMotors"]]

        # <------  Store active data into variables for last 7 days  ---------->
        total_count_7 = [data7["count"]["facebook"], data7["count"]["heyCars"], data7["count"]["autoTrader"], data7["count"]["gumtree"], data7["count"]["motors"]]

        last_7_hours= [total_active_7, total_nonactive_7, total_count_7]
        
        return last_7_hours,data7


    # @st.cache_resource(ttl=86400)
    def last15days():
        
        # <------ Call API for last 15 days data ---------->
        url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=15"
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)

        # <------ If API server give 502 error  ---------->
        while response.status_code == 502:
            print('Again hitting API because API response is "502"')
            response = requests.request("GET", url, headers=headers)
            print("\n\n\nStatus code::::",response.status_code)
            # data15= json.loads(response.text)['data']
            
        data15= json.loads(response.text)['data']
        print("Data 15 days: ",data15)
        
        # <------  Store active data into variables for last 15 days  ---------->
        total_active_15 = [data15["count"]["activeFacebook"],data15["count"]["activeHeyCars"],data15["count"]["activeAutoTrader"],data15["count"]["activeGumtree"],data15["count"]["activeMotors"]]

        # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
        total_nonactive_15 = [data15["checkerActivity"]["deactivatedCountFacebook"], data15["checkerActivity"]["deactivatedCountHeyCars"], data15["checkerActivity"]["deactivatedCountAutoTrader"], data15["checkerActivity"]["deactivatedCountGumtree"], data15["checkerActivity"]["deactivatedCountMotors"]]

        # <------  Store all count data into variables for 24 hours  ---------->
        total_count_15 = [data15["count"]["facebook"], data15["count"]["heyCars"], data15["count"]["autoTrader"], data15["count"]["gumtree"], data15["count"]["motors"]]

        last_15= [total_active_15, total_nonactive_15, total_count_15]
        
        return last_15,data15



    # @st.cache_resource(ttl=86400)
    def last30days():

        # <------ Call API for last 30 days data ---------->
        url = "http://api.aicarz.com/api/v1/dev/data-dashboard?days=30"
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)

        # <------ If API server give 502 error  ---------->
        while response.status_code == 502:
            print('Again hitting API because API response is "502"')
            response = requests.request("GET", url, headers=headers)
            print("\n\n\nStatus code::::",response.status_code)
            # data30= json.loads(response.text)['data']
            
        data30= json.loads(response.text)['data']
        print("Data 30 days: ",data30)
        
        # <------  Store active data into variables for last 15 days  ---------->
        total_active_30 = [data30["count"]["activeFacebook"],data30["count"]["activeHeyCars"],data30["count"]["activeAutoTrader"],data30["count"]["activeGumtree"],data30["count"]["activeMotors"]]

        # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
        total_nonactive_30 = [data30["checkerActivity"]["deactivatedCountFacebook"], data30["checkerActivity"]["deactivatedCountHeyCars"], data30["checkerActivity"]["deactivatedCountAutoTrader"], data30["checkerActivity"]["deactivatedCountGumtree"], data30["checkerActivity"]["deactivatedCountMotors"]]

        # <------  Store all count data into variables for 24 hours  ---------->
        total_count_30 = [data30["count"]["facebook"], data30["count"]["heyCars"], data30["count"]["autoTrader"], data30["count"]["gumtree"], data30["count"]["motors"]]

        last_30= [total_active_30, total_nonactive_30, total_count_30]
        
        return last_30,data30



    # @st.cache_resource(ttl=86400)
    def lifetime():

        # <------ Call API for last lifetime data ---------->
        url = "http://api.aicarz.com/api/v1/dev/data-dashboard"
        response = requests.request("GET", url, headers=headers)
        print("\n\n\nStatus code::::",response.status_code)

        # <------ If API server give 502 error  ---------->
        while response.status_code == 502:
            print('Again hitting API because API response is "502"')
            response = requests.request("GET", url, headers=headers)
            print("\n\n\nStatus code::::",response.status_code)
            # data_lifetime= json.loads(response.text)['data']
            
        data_lifetime= json.loads(response.text)['data']
        print("Data 30 days: ",data_lifetime)
        
        # <------  Store active data into variables for last 15 days  ---------->
        total_active_lifetime = [data_lifetime["count"]["activeFacebook"],data_lifetime["count"]["activeHeyCars"],data_lifetime["count"]["activeAutoTrader"],data_lifetime["count"]["activeGumtree"],data_lifetime["count"]["activeMotors"]]

        # <------  Store deactive data count into variables which deactivated in last 24 hours  ---------->
        total_nonactive_lifetime = [data_lifetime["checkerActivity"]["deactivatedCountFacebook"], data_lifetime["checkerActivity"]["deactivatedCountHeyCars"], data_lifetime["checkerActivity"]["deactivatedCountAutoTrader"], data_lifetime["checkerActivity"]["deactivatedCountGumtree"], data_lifetime["checkerActivity"]["deactivatedCountMotors"]]

        # <------  Store all count data into variables for 24 hours  ---------->
        total_count_lifetime = [data_lifetime["count"]["facebook"], data_lifetime["count"]["heyCars"], data_lifetime["count"]["autoTrader"], data_lifetime["count"]["gumtree"], data_lifetime["count"]["motors"]]

        last_lifetime= [total_active_lifetime, total_nonactive_lifetime, total_count_lifetime]
        
        return last_lifetime,data_lifetime






    # <------ Dropdown to select the data set ---------->
    dataset_name = st.selectbox('Select a Dataset', ['Lifetime', 'Last 30 days','Last 15 days', 'Last 7 days', 'Last 24 Hours'])

    display= False
    if dataset_name == 'Last 24 Hours':
        load1=st.button('Display')
        if load1:
            display= True
            _24hours,data= last24hours()
            data_active = {'Last 24 Hours': _24hours[0]}
            data_nonactive = {'Last 24 Hours': _24hours[1]}
            data_total = {'Last 24 Hours': _24hours[2]}
        
    elif dataset_name == 'Last 7 days':
        load2= st.button('Display')
        if load2:
            display= True
            last7,data= last7days()
            data_active = {'Last 7 days': last7[0]}
            data_nonactive = {'Last 7 days': last7[1]}
            data_total = {'Last 7 days': last7[2]}
        
    elif dataset_name == 'Last 15 days':
        load3= st.button('Display')
        if load3:
            display= True
            last15,data= last15days()
            data_active = {'Last 15 days': last15[0]}
            data_nonactive = {'Last 15 days': last15[1]}
            data_total = {'Last 15 days': last15[2]}

    elif dataset_name == 'Last 30 days':
        load4= st.button('Display')
        if load4:
            display= True
            last30,data= last30days()
            data_active = {'Last 30 days': last30[0]}
            data_nonactive = {'Last 30 days': last30[1]}
            data_total = {'Last 30 days': last30[2]}
        
    else:
        load5= st.button('Display')
        if load5:
            display= True
            lifetime_,data= lifetime()
            data_active = {'Lifetime': lifetime_[0]}
            data_nonactive = {'Lifetime': lifetime_[1]}
            data_total = {'Lifetime': lifetime_[2]}
        
    if display == True:    
        # <------ divide layout into three columns ---------->
        left, center, right = st.columns(3)   
        # st.balloons()
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
                plt.legend([ "Facebook", "Heycars","Autotraders","Gumtree", "Motors"], loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

                # <------  To display donut graph -------->
                st.pyplot(fig1) 
            except:
                pass
            
            # <------  To display actual numbers of records -------->
            st.markdown(f"Total number of active data for {dataset_name} on *Autotraders* is **{data_active[dataset_name][2]}**.")
            st.markdown(f"Total number of active data for {dataset_name} on *Gumtree* is **{data_active[dataset_name][3]}**.")
            st.markdown(f"Total number of active data for {dataset_name} on *Facebook* is **{data_active[dataset_name][0]}**.")
            st.markdown(f"Total number of active data for {dataset_name} on *Motors* is **{data_active[dataset_name][4]}**.")
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
                
                plt.legend([ "Facebook", "Heycars","Autotraders", "Gumtree","Motors"], loc="lower left", bbox_to_anchor=(1, 0, 1, 1))
                
                # <------  To display donut graph -------->
                st.pyplot(fig1)
            except:
                pass
            
            # <------  To display actual numbers of records -------->
            st.markdown(f"Total number of non-active data for {dataset_name} on *Autotraders* is **{data_nonactive[dataset_name][2]}**.")
            st.markdown(f"Total number of non-active data for {dataset_name} on *Gumtree* is **{data_nonactive[dataset_name][3]}**.")
            st.markdown(f"Total number of non-active data for {dataset_name} on *Facebook* is **{data_nonactive[dataset_name][0]}**.")
            st.markdown(f"Total number of non-active data for {dataset_name} on *Motors* is **{data_nonactive[dataset_name][4]}**.")
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
                plt.legend([ "Facebook", "Heycars", "Autotraders","Gumtree","Motors"], loc="lower left", bbox_to_anchor=(1, 0, 1, 1))
                # Display the pie chart
                st.pyplot(fig1)
            except:
                pass
            st.markdown(f"Total number of non-active & active data for {dataset_name} on *Autotraders* is **{data_total[dataset_name][2]}**.")
            st.markdown(f"Total number of non-active & active data for {dataset_name} on *Gumtree* is **{data_total[dataset_name][3]}**.")
            st.markdown(f"Total number of non-active & active data for {dataset_name} on *Facebook* is **{data_total[dataset_name][0]}**.")
            st.markdown(f"Total number of non-active & active data for {dataset_name} on *Motors* is **{data_total[dataset_name][4]}**.")
            st.markdown(f"Total number of non-active & active data for {dataset_name} on *Heycars* is **{data_total[dataset_name][1]}**.")
            st.markdown(f"Total number of non-active & active data for {dataset_name} on all *Platforms* is **{data_total[dataset_name][1] + data_total[dataset_name][4] + data_total[dataset_name][0] + data_total[dataset_name][3] + data_total[dataset_name][2]}**.")


        st.header("Data Stats (Active)")
        st.markdown("-------------------------------------------------------------------------------")


        left,centerleft,centerright, right = st.columns(4)   

        with left:
            st.markdown(f"Total data onboard: **{format( data['count']['totalCount'], ',')}**")
            # st.subheader(f"Last day data onboard: {753256}")
            # st.subheader(f"No. of data failure: {753256}")
            fuel_dict=data['active']['topLargestInventoryFuelType']
            def sort_by_value(item):
                return item[1]

            sorted_fuel_with_count = dict(sorted(fuel_dict.items(), key=sort_by_value, reverse=True))

            sorted_fuel= list(sorted_fuel_with_count.keys())
            sorted_fuel_count= list(sorted_fuel_with_count.values())
            
            # Displaying in Streamlit
            st.markdown(f"Most frequent active fuel type: **{sorted_fuel[0]}** (Count: **{sorted_fuel_count[0]}**)")
            st.markdown("-------------------------------------------------------------------------------")

            # Query to find the minimum price value where isActive is true
            try:
                min_value = format(data['active']['priceMin'], ",")
            except:
                min_value = data['active']['priceMin']
            # Query to find the maximum price value where isActive is true
            
            try:
                max_value = format(data['active']['priceMax'], ",")
            except:
                max_value = data['active']['priceMax']
            print(f"Minimum value: {min_value}")
            print(f"Maximum value: {max_value}")

            # Displaying in Streamlit
            st.markdown(f"Max price in active data: **{max_value}£**")
            st.markdown(f"Min price in active data: **{min_value}£**")
            st.markdown("-------------------------------------------------------------------------------")

        # Adjusting queries to exclude documents where 'engineSizeInLiter' is None
        # Query to find the minimum engine size in liters where isActive is true and engineSizeInLiter is not None
        min_value = data['active']['engineSizeInLiterMin']

        # Query to find the maximum engine size in liters where isActive is true and engineSizeInLiter is not None
        max_value = data['active']['engineSizeInLiterMax']

        with centerleft:
            # Displaying in Streamlit
            if max_value is not None:
                st.markdown(f"Max engine size in liter in active data: **{max_value}**")

            if min_value is not None:
                st.markdown(f"Min engine size in liter in active data: **{min_value}**")
            st.markdown("-------------------------------------------------------------------------------")



            # Query to find the minimum makeYear where isActive is true and makeYear is not None
            min_value = data['active']['yearMin']

            # Query to find the maximum makeYear where isActive is true and makeYear is not None
            max_value = data['active']['yearMax']

            # Displaying in Streamlit

            st.markdown(f"Max year in active data: **{max_value}**")

            st.markdown(f"Min year in active data: **{min_value}**")
            st.markdown("-------------------------------------------------------------------------------")

        with centerright:

            # Query to find the minimum mileageInMiles where isActive is true and mileageInMiles is not None
            min_value = format(data['active']['milageMin'], ',')

            # Query to find the maximum mileageInMiles where isActive is true and mileageInMiles is not None
            max_value = format(data['active']['milageMax'], ',')

            # Displaying in Streamlit
            st.markdown(f"Max mileage in active data: **{max_value}** miles")
            st.markdown(f"Min mileage in active data: **{min_value}** miles")



            st.markdown("-------------------------------------------------------------------------------")


            # Displaying in Streamlit
            try:
                st.markdown(f"Total number of unique active makes: **{data['active']['distinctMakeCount']}**")
            except:
                pass
            # st.markdown("-------------------------------------------------------------------------------")


            # Displaying in Streamlit
            try:
                st.markdown(f"Total number of unique active model: **{data['active']['distinctModelCount']}**")
            except:
                pass
            st.markdown("-------------------------------------------------------------------------------")

        with right:

            make_dict=data['active']['topLargestInventoryMake']
            def sort_by_value(item):
                return item[1]

            sorted_make_with_count = dict(sorted(make_dict.items(), key=sort_by_value, reverse=True))
            
            sorted_make= list(sorted_make_with_count.keys())
            sorted_make_count = list(sorted_make_with_count.values())
            
            # Displaying in Streamlit
            try:
                st.markdown(f"Top 1st largest make on inventory: **{sorted_make[0]}** (Count: **{sorted_make_count[0]}**)")
            except:
                pass
            try:
                st.markdown(f"Top 2nd largest make on inventory: **{sorted_make[1]}** (Count: **{sorted_make_count[1]}**)")
            except:
                pass
            try:
                st.markdown(f"Top 3rd largest make on inventory: **{sorted_make[2]}** (Count: **{sorted_make_count[2]}**)")
            except:
                pass
            try:
                st.markdown(f"Top 4th largest make on inventory: **{sorted_make[3]}** (Count: **{sorted_make_count[3]}**)")
            except:
                pass
            try:
                st.markdown(f"Top 5th largest make on inventory: **{sorted_make[4]}** (Count: **{sorted_make_count[4]}**)")
            except:
                pass
            st.markdown("-------------------------------------------------------------------------------")


            
        load=False
except:
    st.title("Something Went Wront. Please **refresh** this page or revisit later")