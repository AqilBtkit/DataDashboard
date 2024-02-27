import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pymongo
from datetime import datetime, tzinfo, timezone


st.set_page_config(layout="wide")

st.title("Data Dashboard")
# st.markdown("**________________________________________________________________________________________________________________________________________________________________________________**")
st.header(f"Platforms")


connection_string = "mongodb+srv://web_scrapping_read_only:rVXnGzz3jZvnRZx1@cluster0.uarux4m.mongodb.net/?retryWrites=true&w=majority"
mongodbConn = pymongo.MongoClient(connection_string)
carzdb = mongodbConn["aicarsdb"]
collection = carzdb["cars"]

# Sample data

twenty_four_hours_ago = datetime.now() - timedelta(hours=24)

query_facebook_24 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": twenty_four_hours_ago},
    "isActive": True
    }
total_active_facebook_24 = collection.count_documents(query_facebook_24)

query_heycar_24 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": twenty_four_hours_ago},
    "isActive": True
    }
total_active_heycar_24 = collection.count_documents(query_heycar_24)

query_autotrader_24 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": twenty_four_hours_ago},
    "isActive": True
    }
total_active_autotrader_24 = collection.count_documents(query_autotrader_24)

query_gumtree_24 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": twenty_four_hours_ago},
    "isActive": True
    }
total_active_gumtree_24 = collection.count_documents(query_gumtree_24)

query_motors_24 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": twenty_four_hours_ago},
    "isActive": True
    }
total_active_motors_24 = collection.count_documents(query_motors_24)




seven_days_ago = datetime.now() - timedelta(hours=168)

query_facebook_7 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": seven_days_ago},
    "isActive": True
    }
total_active_facebook_7 = collection.count_documents(query_facebook_7)

query_heycar_7 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": seven_days_ago},
    "isActive": True
    }
total_active_heycar_7 = collection.count_documents(query_heycar_7)

query_autotrader_7 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": seven_days_ago},
    "isActive": True
    }
total_active_autotrader_7 = collection.count_documents(query_autotrader_7)

query_gumtree_7 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": seven_days_ago},
    "isActive": True
    }
total_active_gumtree_7 = collection.count_documents(query_gumtree_7)

query_motors_7 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": seven_days_ago},
    "isActive": True
    }
total_active_motors_7 = collection.count_documents(query_motors_7)





_15_days_ago = datetime.now() - timedelta(hours=360)

query_facebook_15 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": _15_days_ago},
    "isActive": True
    }
total_active_facebook_15 = collection.count_documents(query_facebook_15)

query_heycar_15 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": _15_days_ago},
    "isActive": True
    }
total_active_heycar_15 = collection.count_documents(query_heycar_15)

query_autotrader_15 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": _15_days_ago},
    "isActive": True
    }
total_active_autotrader_15 = collection.count_documents(query_autotrader_15)

query_gumtree_15 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": _15_days_ago},
    "isActive": True
    }
total_active_gumtree_15 = collection.count_documents(query_gumtree_15)

query_motors_15 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": _15_days_ago},
    "isActive": True
    }
total_active_motors_15 = collection.count_documents(query_motors_15)





_30_days_ago = datetime.now() - timedelta(hours=720)

query_facebook_30 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": _30_days_ago},
    "isActive": True
    }
total_active_facebook_30 = collection.count_documents(query_facebook_30)

query_heycar_30 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": _30_days_ago},
    "isActive": True
    }
total_active_heycar_30 = collection.count_documents(query_heycar_30)

query_autotrader_30 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": _30_days_ago},
    "isActive": True
    }
total_active_autotrader_30 = collection.count_documents(query_autotrader_30)

query_gumtree_30 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": _30_days_ago},
    "isActive": True
    }
total_active_gumtree_30 = collection.count_documents(query_gumtree_30)

query_motors_30 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": _30_days_ago},
    "isActive": True
    }
total_active_motors_30 = collection.count_documents(query_motors_30)





query_facebook = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "isActive": True
    }
total_active_facebook = collection.count_documents(query_facebook)

query_heycar = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "isActive": True
    }
total_active_heycar = collection.count_documents(query_heycar)

query_autotrader = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "isActive": True
    }
total_active_autotrader = collection.count_documents(query_autotrader)

query_gumtree = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "isActive": True
    }
total_active_gumtree = collection.count_documents(query_gumtree)

query_motors = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "isActive": True
    }
total_active_motors = collection.count_documents(query_motors)


data = {
    'Last 24 Hours': [total_active_autotrader_24, total_active_gumtree_24, total_active_facebook_24, total_active_heycar_24, total_active_motors_24],
    'Last 7 days': [total_active_autotrader_7, total_active_gumtree_7, total_active_facebook_7, total_active_heycar_7, total_active_motors_7],
    'Last 15 days': [total_active_autotrader_15, total_active_gumtree_15, total_active_facebook_15, total_active_heycar_15, total_active_motors_15],
    'Last 30 days': [total_active_autotrader_30, total_active_gumtree_30, total_active_facebook_30, total_active_heycar_30, total_active_motors_30],
    'Lifetime': [total_active_autotrader, total_active_gumtree, total_active_facebook, total_active_heycar, total_active_motors]
}
df = pd.DataFrame(data, index=["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"])


# Dropdown to select the data set
dataset_name = st.selectbox('Select a Dataset', df.columns)

left,center, right = st.columns(3)   
with left:   
    st.subheader(f"Active:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#BB33FF']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    # Create a pie chart for the selected data set
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
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
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # Add a legend
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        st.pyplot(fig1) 
    except:
        pass

    st.markdown(f"Total number of active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Autotraders']}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Gumtree']}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Facebook']}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Moters* is **{df[dataset_name]['Moters']}**.")
    st.markdown(f"Total number of active data for {dataset_name} on *Heycars* is **{df[dataset_name]['Heycars']}**.")
    st.markdown(f"Total number of active data for {dataset_name} on all *Platforms* is **{df[dataset_name]['Heycars']+df[dataset_name]['Moters']+df[dataset_name]['Facebook']+df[dataset_name]['Gumtree']+df[dataset_name]['Autotraders']}**.")
    # st.markdown("-------------------------------------------------------------------------------")
    # Sample data
    # Sample data

twenty_four_hours_ago = datetime.now() - timedelta(hours=24)

query_facebook_24 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "deActivatedAt": {"$gte": twenty_four_hours_ago},
    "isActive": False
    }
total_nonactive_facebook_24 = collection.count_documents(query_facebook_24)

query_heycar_24 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "deActivatedAt": {"$gte": twenty_four_hours_ago},
    "isActive": False
    }
total_nonactive_heycar_24 = collection.count_documents(query_heycar_24)

query_autotrader_24 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "deActivatedAt": {"$gte": twenty_four_hours_ago},
    "isActive": False
    }
total_nonactive_autotrader_24 = collection.count_documents(query_autotrader_24)

query_gumtree_24 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "deActivatedAt": {"$gte": twenty_four_hours_ago},
    "isActive": False
    }
total_nonactive_gumtree_24 = collection.count_documents(query_gumtree_24)

query_motors_24 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "deActivatedAt": {"$gte": twenty_four_hours_ago},
    "isActive": False
    }
total_nonactive_motors_24 = collection.count_documents(query_motors_24)




seven_days_ago = datetime.now() - timedelta(hours=168)

query_facebook_7 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "deActivatedAt": {"$gte": seven_days_ago},
    "isActive": False
    }
total_nonactive_facebook_7 = collection.count_documents(query_facebook_7)

query_heycar_7 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "deActivatedAt": {"$gte": seven_days_ago},
    "isActive": False
    }
total_nonactive_heycar_7 = collection.count_documents(query_heycar_7)

query_autotrader_7 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "deActivatedAt": {"$gte": seven_days_ago},
    "isActive": False
    }
total_nonactive_autotrader_7 = collection.count_documents(query_autotrader_7)

query_gumtree_7 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "deActivatedAt": {"$gte": seven_days_ago},
    "isActive": False
    }
total_nonactive_gumtree_7 = collection.count_documents(query_gumtree_7)

query_motors_7 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "deActivatedAt": {"$gte": seven_days_ago},
    "isActive": False
    }
total_nonactive_motors_7 = collection.count_documents(query_motors_7)





_15_days_ago = datetime.now() - timedelta(hours=360)

query_facebook_15 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "deActivatedAt": {"$gte": _15_days_ago},
    "isActive": False
    }
total_nonactive_facebook_15 = collection.count_documents(query_facebook_15)

query_heycar_15 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "deActivatedAt": {"$gte": _15_days_ago},
    "isActive": False
    }
total_nonactive_heycar_15 = collection.count_documents(query_heycar_15)

query_autotrader_15 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "deActivatedAt": {"$gte": _15_days_ago},
    "isActive": False
    }
total_nonactive_autotrader_15 = collection.count_documents(query_autotrader_15)

query_gumtree_15 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "deActivatedAt": {"$gte": _15_days_ago},
    "isActive": False
    }
total_nonactive_gumtree_15 = collection.count_documents(query_gumtree_15)

query_motors_15 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "deActivatedAt": {"$gte": _15_days_ago},
    "isActive": False
    }
total_nonactive_motors_15 = collection.count_documents(query_motors_15)





_30_days_ago = datetime.now() - timedelta(hours=720)

query_facebook_30 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "deActivatedAt": {"$gte": _30_days_ago},
    "isActive": False
    }
total_nonactive_facebook_30 = collection.count_documents(query_facebook_30)

query_heycar_30 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "deActivatedAt": {"$gte": _30_days_ago},
    "isActive": False
    }
total_nonactive_heycar_30 = collection.count_documents(query_heycar_30)

query_autotrader_30 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "deActivatedAt": {"$gte": _30_days_ago},
    "isActive": False
    }
total_nonactive_autotrader_30 = collection.count_documents(query_autotrader_30)

query_gumtree_30 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "deActivatedAt": {"$gte": _30_days_ago},
    "isActive": False
    }
total_nonactive_gumtree_30 = collection.count_documents(query_gumtree_30)

query_motors_30 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "deActivatedAt": {"$gte": _30_days_ago},
    "isActive": False
    }
total_nonactive_motors_30 = collection.count_documents(query_motors_30)





query_facebook = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "isActive": False
    }
total_nonactive_facebook = collection.count_documents(query_facebook)

query_heycar = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "isActive": False
    }
total_nonactive_heycar = collection.count_documents(query_heycar)

query_autotrader = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "isActive": False
    }
total_nonactive_autotrader = collection.count_documents(query_autotrader)

query_gumtree = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "isActive": False
    }
total_nonactive_gumtree = collection.count_documents(query_gumtree)

query_motors = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "isActive": False
    }
total_nonactive_motors = collection.count_documents(query_motors)


data = {
    'Last 24 Hours': [total_nonactive_autotrader_24, total_nonactive_gumtree_24, total_nonactive_facebook_24, total_nonactive_heycar_24, total_nonactive_motors_24],
    'Last 7 days': [total_nonactive_autotrader_7, total_nonactive_gumtree_7, total_nonactive_facebook_7, total_nonactive_heycar_7, total_nonactive_motors_7],
    'Last 15 days': [total_nonactive_autotrader_15, total_nonactive_gumtree_15, total_nonactive_facebook_15, total_nonactive_heycar_15, total_nonactive_motors_15],
    'Last 30 days': [total_nonactive_autotrader_30, total_nonactive_gumtree_30, total_nonactive_facebook_30, total_nonactive_heycar_30, total_nonactive_motors_30],
    'Lifetime': [total_nonactive_autotrader, total_nonactive_gumtree, total_nonactive_facebook, total_nonactive_heycar, total_nonactive_motors]
    }

df = pd.DataFrame(data, index=["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"])

# Dropdown to select the data set
# dataset_name = st.selectbox('Select a Dataset', df.columns)
with center:
    st.subheader(f"Deactive:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#BB33FF']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    print(df[dataset_name])
    # Create a pie chart for the selected data set 
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
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
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))
        # Display the pie chart
        st.pyplot(fig1)
        # Create a pie chart for the selected data set
    except:
        pass
    st.markdown(f"Total number of non-active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Autotraders']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Gumtree']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Facebook']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Moters* is **{df[dataset_name]['Moters']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Heycars* is **{df[dataset_name]['Heycars']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on all *Platforms* is **{df[dataset_name]['Heycars']+df[dataset_name]['Moters']+df[dataset_name]['Facebook']+df[dataset_name]['Gumtree']+df[dataset_name]['Autotraders']}**.")
    # st.markdown("-------------------------------------------------------------------------------")





# Sample data



twenty_four_hours_ago = datetime.now() - timedelta(hours=24)

query_facebook_24 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": twenty_four_hours_ago}
    }
total_count_facebook_24 = collection.count_documents(query_facebook_24)

query_heycar_24 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": twenty_four_hours_ago}
    }
total_count_heycar_24 = collection.count_documents(query_heycar_24)

query_autotrader_24 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": twenty_four_hours_ago}
    }
total_count_autotrader_24 = collection.count_documents(query_autotrader_24)

query_gumtree_24 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": twenty_four_hours_ago}
    }
total_count_gumtree_24 = collection.count_documents(query_gumtree_24)

query_motors_24 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": twenty_four_hours_ago}
    }
total_count_motors_24 = collection.count_documents(query_motors_24)




seven_days_ago = datetime.now() - timedelta(hours=168)

query_facebook_7 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": seven_days_ago}
    }
total_count_facebook_7 = collection.count_documents(query_facebook_7)

query_heycar_7 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": seven_days_ago}
    }
total_count_heycar_7 = collection.count_documents(query_heycar_7)

query_autotrader_7 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": seven_days_ago}
    }
total_count_autotrader_7 = collection.count_documents(query_autotrader_7)

query_gumtree_7 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": seven_days_ago}
    }
total_count_gumtree_7 = collection.count_documents(query_gumtree_7)

query_motors_7 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": seven_days_ago}
    }
total_count_motors_7 = collection.count_documents(query_motors_7)





_15_days_ago = datetime.now() - timedelta(hours=360)

query_facebook_15 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": _15_days_ago}
    }
total_count_facebook_15 = collection.count_documents(query_facebook_15)

query_heycar_15 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": _15_days_ago}
    }
total_count_heycar_15 = collection.count_documents(query_heycar_15)

query_autotrader_15 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": _15_days_ago}
    }
total_count_autotrader_15 = collection.count_documents(query_autotrader_15)

query_gumtree_15 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": _15_days_ago}
    }
total_count_gumtree_15 = collection.count_documents(query_gumtree_15)

query_motors_15 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": _15_days_ago}
    }
total_count_motors_15 = collection.count_documents(query_motors_15)





_30_days_ago = datetime.now() - timedelta(hours=720)

query_facebook_30 = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"},
    "createdOn": {"$gte": _30_days_ago}
    }
total_count_facebook_30 = collection.count_documents(query_facebook_30)

query_heycar_30 = {
    "carBuyLink": {"$regex": "^https://heycar.com"},
    "createdOn": {"$gte": _30_days_ago}
    }
total_count_heycar_30 = collection.count_documents(query_heycar_30)

query_autotrader_30 = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"},
    "createdOn": {"$gte": _30_days_ago}
    }
total_count_autotrader_30 = collection.count_documents(query_autotrader_30)

query_gumtree_30 = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"},
    "createdOn": {"$gte": _30_days_ago}
    }
total_count_gumtree_30 = collection.count_documents(query_gumtree_30)

query_motors_30 = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"},
    "createdOn": {"$gte": _30_days_ago}
    }
total_count_motors_30 = collection.count_documents(query_motors_30)





query_facebook = {
    "carBuyLink": {"$regex": "^https://www.facebook.com"}
    }
total_count_facebook = collection.count_documents(query_facebook)

query_heycar = {
    "carBuyLink": {"$regex": "^https://heycar.com"}
    }
total_count_heycar = collection.count_documents(query_heycar)

query_autotrader = {
    "carBuyLink": {"$regex": "^https://www.autotrader.co.uk"}
    }
total_count_autotrader = collection.count_documents(query_autotrader)

query_gumtree = {
    "carBuyLink": {"$regex": "^https://www.gumtree.com"}
    }
total_count_gumtree = collection.count_documents(query_gumtree)

query_motors = {
    "carBuyLink": {"$regex": "^https://www.motors.co.uk/"}
    }
total_count_motors = collection.count_documents(query_motors)


data = {
    'Last 24 Hours': [total_count_autotrader_24, total_count_gumtree_24, total_count_facebook_24, total_count_heycar_24, total_count_motors_24],
    'Last 7 days': [total_count_autotrader_7, total_count_gumtree_7, total_count_facebook_7, total_count_heycar_7, total_count_motors_7],
    'Last 15 days': [total_count_autotrader_15, total_count_gumtree_15, total_count_facebook_15, total_count_heycar_15, total_count_motors_15],
    'Last 30 days': [total_count_autotrader_30, total_count_gumtree_30, total_count_facebook_30, total_count_heycar_30, total_count_motors_30],
    'Lifetime': [total_count_autotrader, total_count_gumtree, total_count_facebook, total_count_heycar, total_count_motors]
    }
df = pd.DataFrame(data, index=["Autotraders", "Gumtree","Facebook", "Heycars", "Moters"])

# Dropdown to select the data set
# dataset_name = st.selectbox('Select a Dataset', df.columns)
with right:
    st.subheader(f"Total:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#BB33FF']   


    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''

    try:
        # Create a pie chart for the selected data set
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
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
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))
        # Display the pie chart
        st.pyplot(fig1)
    except:
        pass
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Autotraders']}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Gumtree']}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Facebook']}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Moters* is **{df[dataset_name]['Moters']}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on *Heycars* is **{df[dataset_name]['Heycars']}**.")
    st.markdown(f"Total number of non-active & active data for {dataset_name} on all *Platforms* is **{df[dataset_name]['Heycars']+df[dataset_name]['Moters']+df[dataset_name]['Facebook']+df[dataset_name]['Gumtree']+df[dataset_name]['Autotraders']}**.")


data = {
    'Last 24 Hours': [total_active_autotrader_24,total_nonactive_autotrader_24],
    'Last 7 days': [total_active_autotrader_7, total_nonactive_autotrader_7],
    'Last 15 days': [total_active_autotrader_15, total_nonactive_autotrader_15],
    'Last 30 days': [total_active_autotrader_30, total_nonactive_autotrader_30],
    'Lifetime': [total_active_autotrader, total_nonactive_autotrader]
}
df = pd.DataFrame(data, index=["Active", "Non-Active"])


# Dropdown to select the data set
dataset_name = st.selectbox('Select a Dataset', df.columns)

# left,center, right = st.columns(3)   
with left:   
    st.subheader(f"Autotraders:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    # Create a pie chart for the selected data set
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
                colors=colors, 
                # labels=df.index, 
                autopct=custom_autopct, 
                # startangle= 90,
                pctdistance=0.85,
                explode=(0, 0),  # Exploding the first slice
                # shadow=True
                counterclock=False
                )

        # Draw a circle at the center to make it look like a donut
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # Add a legend
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        st.pyplot(fig1) 
    except:
        pass

    st.markdown(f"Total number of active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Active']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Autotraders* is **{df[dataset_name]['Non-Active']}**.")
    st.markdown(f"Total number of data for {dataset_name} on all *Autotraders* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")


data = {
    'Last 24 Hours': [total_active_gumtree_24,total_nonactive_gumtree_24],
    'Last 7 days': [total_active_gumtree_7, total_nonactive_gumtree_7],
    'Last 15 days': [total_active_gumtree_15, total_nonactive_gumtree_15],
    'Last 30 days': [total_active_gumtree_30, total_nonactive_gumtree_30],
    'Lifetime': [total_active_gumtree, total_nonactive_gumtree]
}
df = pd.DataFrame(data, index=["Active", "Non-Active"])


# Dropdown to select the data set
dataset_name = st.selectbox('Select a Dataset', df.columns)

with center:   
    st.subheader(f"Gumtree:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    # Create a pie chart for the selected data set
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
                colors=colors, 
                # labels=df.index, 
                autopct=custom_autopct, 
                # startangle= 90,
                pctdistance=0.85,
                explode=(0, 0),  # Exploding the first slice
                # shadow=True
                counterclock=False
                )

        # Draw a circle at the center to make it look like a donut
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # Add a legend
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        st.pyplot(fig1) 
    except:
        pass

    st.markdown(f"Total number of active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Active']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Gumtree* is **{df[dataset_name]['Non-Active']}**.")
    st.markdown(f"Total number of data for {dataset_name} on all *Gumtree* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    


data = {
    'Last 24 Hours': [total_active_facebook_24,total_nonactive_facebook_24],
    'Last 7 days': [total_active_facebook_7, total_nonactive_facebook_7],
    'Last 15 days': [total_active_facebook_15, total_nonactive_facebook_15],
    'Last 30 days': [total_active_facebook_30, total_nonactive_facebook_30],
    'Lifetime': [total_active_facebook, total_nonactive_facebook]
}
df = pd.DataFrame(data, index=["Active", "Non-Active"])


# Dropdown to select the data set
dataset_name = st.selectbox('Select a Dataset', df.columns)

with right:   
    st.subheader(f"Facebook:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    # Create a pie chart for the selected data set
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
                colors=colors, 
                # labels=df.index, 
                autopct=custom_autopct, 
                # startangle= 90,
                pctdistance=0.85,
                explode=(0, 0),  # Exploding the first slice
                # shadow=True
                counterclock=False
                )

        # Draw a circle at the center to make it look like a donut
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # Add a legend
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        st.pyplot(fig1) 
    except:
        pass

    st.markdown(f"Total number of active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Active']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Facebook* is **{df[dataset_name]['Non-Active']}**.")
    st.markdown(f"Total number of data for {dataset_name} on all *Facebook* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    

data = {
    'Last 24 Hours': [total_active_heycar_24,total_nonactive_heycar_24],
    'Last 7 days': [total_active_heycar_7, total_nonactive_heycar_7],
    'Last 15 days': [total_active_heycar_15, total_nonactive_heycar_15],
    'Last 30 days': [total_active_heycar_30, total_nonactive_heycar_30],
    'Lifetime': [total_active_heycar, total_nonactive_heycar]
}
df = pd.DataFrame(data, index=["Active", "Non-Active"])


# Dropdown to select the data set
dataset_name = st.selectbox('Select a Dataset', df.columns)

with left:   
    st.subheader(f"Heycar:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    # Create a pie chart for the selected data set
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
                colors=colors, 
                # labels=df.index, 
                autopct=custom_autopct, 
                # startangle= 90,
                pctdistance=0.85,
                explode=(0, 0),  # Exploding the first slice
                # shadow=True
                counterclock=False
                )

        # Draw a circle at the center to make it look like a donut
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # Add a legend
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        st.pyplot(fig1) 
    except:
        pass

    st.markdown(f"Total number of active data for {dataset_name} on *Heycar* is **{df[dataset_name]['Active']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Heycar* is **{df[dataset_name]['Non-Active']}**.")
    st.markdown(f"Total number of data for {dataset_name} on all *Heycar* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    

data = {
    'Last 24 Hours': [total_active_heycar_24,total_nonactive_heycar_24],
    'Last 7 days': [total_active_heycar_7, total_nonactive_heycar_7],
    'Last 15 days': [total_active_heycar_15, total_nonactive_heycar_15],
    'Last 30 days': [total_active_heycar_30, total_nonactive_heycar_30],
    'Lifetime': [total_active_heycar, total_nonactive_heycar]
}
df = pd.DataFrame(data, index=["Active", "Non-Active"])


# Dropdown to select the data set
dataset_name = st.selectbox('Select a Dataset', df.columns)

with right:   
    st.subheader(f"Heycar:")
    # Custom color palette
    colors = ['#ff9999','#66b3ff']

    def custom_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 1 else ''
    # Create a pie chart for the selected data set
    try:   
        fig1, ax1 = plt.subplots()
        ax1.pie(df[dataset_name], 
                colors=colors, 
                # labels=df.index, 
                autopct=custom_autopct, 
                # startangle= 90,
                pctdistance=0.85,
                explode=(0, 0),  # Exploding the first slice
                # shadow=True
                counterclock=False
                )

        # Draw a circle at the center to make it look like a donut
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig1.gca().add_artist(centre_circle)

        # Add a legend
        plt.legend(df.index, loc="lower left", bbox_to_anchor=(1, 0, 1, 1))

        st.pyplot(fig1) 
    except:
        pass

    st.markdown(f"Total number of active data for {dataset_name} on *Heycar* is **{df[dataset_name]['Active']}**.")
    st.markdown(f"Total number of non-active data for {dataset_name} on *Heycar* is **{df[dataset_name]['Non-Active']}**.")
    st.markdown(f"Total number of data for {dataset_name} on all *Heycar* is **{df[dataset_name]['Active']+df[dataset_name]['Non-Active']}**.")
    

    # st.markdown("-------------------------------------------------------------------------------")
    # Sample data
    # Sample data
# st.markdown("**________________________________________________________________________________________________________________________________________________________________________________**")
st.header("Data Stats")
st.markdown("-------------------------------------------------------------------------------")


left,centerleft,centerright, right = st.columns(4)   
connection_string = "mongodb+srv://dbuser123:VkzPhWfVCq4mr9M@cluster0.1gvhuro.mongodb.net/?retryWrites=true&w=majority"
mongodbConn = pymongo.MongoClient(connection_string)
carzdb = mongodbConn["aicarsStagingdb"]
collection1 = carzdb["dataNotProcesseed"]
collection2 = carzdb["FBdataNotProcesseed"]


unique_car_buylinks = collection1.distinct("carBuyLink")
unique_car_buylinks2 = collection2.distinct("carBuyLink")

with left:
    st.markdown(f"Data onboard today: **{format(collection.count_documents({'createdOn': {'$gte': twenty_four_hours_ago},}), ',')}**")
    # st.subheader(f"Last day data onboard: {753256}")
    st.markdown(f"No. of Data failure: **{format(len(unique_car_buylinks)+len(unique_car_buylinks2), ',')}**")
    # st.subheader(f"No. of data failure: {753256}")
    st.markdown("-------------------------------------------------------------------------------")

    # Query to find the minimum price value where isActive is true
    min_result = list(collection.find({'isActive': True, 'price': {'$ne': None}}).sort('price', 1).limit(1))
    min_value = format(min_result[0]['price'], ",") if min_result else None


    # Query to find the maximum price value where isActive is true
    max_result = list(collection.find({'isActive': True, 'price': {'$ne': None}}).sort('price', -1).limit(1))
    max_value = format(max_result[0]['price'], ",") if max_result else None

    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")

    # Displaying in Streamlit
    st.markdown(f"Max price in active data: **{max_value}£**")
    st.markdown(f"Min price in active data: **{min_value}£**")
    st.markdown("-------------------------------------------------------------------------------")

# Adjusting queries to exclude documents where 'engineSizeInLiter' is None
# Query to find the minimum engine size in liters where isActive is true and engineSizeInLiter is not None
min_result = list(collection.find({'isActive': True, 'engineSizeInLiter': {'$ne': None}}).sort('engineSizeInLiter', 1).limit(1))
min_value = min_result[0]['engineSizeInLiter'] if min_result else None

# Query to find the maximum engine size in liters where isActive is true and engineSizeInLiter is not None
max_result = list(collection.find({'isActive': True, 'engineSizeInLiter': {'$ne': None}}).sort('engineSizeInLiter', -1).limit(1))
max_value = max_result[0]['engineSizeInLiter'] if max_result else None

with centerleft:
    # Displaying in Streamlit
    if max_value is not None:
        st.markdown(f"Max engine size in liter in active data: **{max_value}**")

    if min_value is not None:
        st.markdown(f"Min engine size in liter in active data: **{min_value}**")
    st.markdown("-------------------------------------------------------------------------------")



    # Query to find the minimum makeYear where isActive is true and makeYear is not None
    min_result = list(collection.find({'isActive': True, 'year': {'$ne': None}}).sort('year', 1).limit(1))
    min_value = min_result[0]['year'] if min_result else None

    # Query to find the maximum makeYear where isActive is true and makeYear is not None
    max_result = list(collection.find({'isActive': True, 'year': {'$ne': None}}).sort('year', -1).limit(1))
    max_value = max_result[0]['year'] if max_result else None

    # Displaying in Streamlit

    st.markdown(f"Max year in active data: **{max_value}**")

    st.markdown(f"Min year in active data: **{min_value}**")
    st.markdown("-------------------------------------------------------------------------------")

with centerright:

    # Query to find the minimum mileageInMiles where isActive is true and mileageInMiles is not None
    min_result = list(collection.find({'isActive': True, 'mileageInMiles': {'$ne': None}}).sort('mileageInMiles', 1).limit(1))
    min_value = format(min_result[0]['mileageInMiles'], ',') if min_result else None

    # Query to find the maximum mileageInMiles where isActive is true and mileageInMiles is not None
    max_result = list(collection.find({'isActive': True, 'mileageInMiles': {'$ne': None}}).sort('mileageInMiles', -1).limit(1))
    max_value = format(max_result[0]['mileageInMiles'], ',') if max_result else None

    # Displaying in Streamlit
    st.markdown(f"Max mileage in active data: **{max_value}** miles")
    st.markdown(f"Min mileage in active data: **{min_value}** miles")



    st.markdown("-------------------------------------------------------------------------------")
    # Aggregation pipeline to count unique makes where isActive is True
    pipeline = [
        {"$match": {"isActive": True}},  # Filter for isActive being True
        {"$group": {"_id": "$make"}},  # Group by the 'make' field
        {"$group": {"_id": None, "uniqueCount": {"$sum": 1}}}  # Count unique makes
    ]

    unique_make_count_result = list(collection.aggregate(pipeline))

    if unique_make_count_result:
        unique_make_count = format(unique_make_count_result[0]['uniqueCount'], ',')
    else:
        unique_make_count = 0

    # Displaying in Streamlit
    st.markdown(f"Total number of unique active makes: **{unique_make_count}**")
    # st.markdown("-------------------------------------------------------------------------------")

    # Aggregation pipeline to count unique makes where isActive is True
    pipeline = [
        {"$match": {"isActive": True}},  # Filter for isActive being True
        {"$group": {"_id": "$model"}},  # Group by the 'model' field
        {"$group": {"_id": None, "uniqueCount": {"$sum": 1}}}  # Count unique makes
    ]

    unique_model_count_result = list(collection.aggregate(pipeline))

    if unique_model_count_result:
        unique_model_count = format(unique_model_count_result[0]['uniqueCount'], ',')
    else:
        unique_model_count = 0

    # Displaying in Streamlit
    st.markdown(f"Total number of unique active model: **{unique_model_count}**")
    st.markdown("-------------------------------------------------------------------------------")

with right:


    # Aggregation pipeline to find the most frequent make where isActive is True
    pipeline = [
        {"$match": {"isActive": True}},  # Filter to include only active makes
        {"$group": {"_id": "$make", "count": {"$sum": 1}}},  # Group by make and count
        {"$sort": {"count": -1}},  # Sort by count in descending order
        {"$limit": 5}  # Limit to the top result
    ]

    most_frequent_make = list(collection.aggregate(pipeline))

    if most_frequent_make:
        make_name1 = most_frequent_make[0]['_id']
        make_count1 = format(most_frequent_make[0]['count'], ',')
    else:
        make_name1 = "None"
        make_count1 = 0

    if most_frequent_make:
        make_name2 = most_frequent_make[1]['_id']
        make_count2 = format(most_frequent_make[1]['count'], ',')
    else:
        make_name2 = "None"
        make_count2 = 0

    if most_frequent_make:
        make_name3 = most_frequent_make[2]['_id']
        make_count3 = format(most_frequent_make[2]['count'], ',')
    else:
        make_name3 = "None"
        make_count3 = 0

    if most_frequent_make:
        make_name4 = most_frequent_make[3]['_id']
        make_count4 = format(most_frequent_make[3]['count'], ',')
    else:
        make_name4 = "None"
        make_count4 = 0

    if most_frequent_make:
        make_name5 = most_frequent_make[4]['_id']
        make_count5 = format(most_frequent_make[4]['count'], ',')
    else:
        make_name5 = "None"
        make_count5 = 0

    # Displaying in Streamlit
    st.markdown(f"Active make on first position: **{make_name1}** (Count: **{make_count1}**)")
    st.markdown(f"Active make on second position: **{make_name2}** (Count: **{make_count2}**)")
    st.markdown(f"Active make on third position: **{make_name3}** (Count: **{make_count3}**)")
    st.markdown(f"Active make on fourth position: **{make_name4}** (Count: **{make_count4}**)")
    st.markdown(f"Active make on fifth position: **{make_name5}** (Count: **{make_count5}**)")

    st.markdown("-------------------------------------------------------------------------------")

    # Aggregation pipeline to find the most frequent fuelType where isActive is True
    pipeline = [
        {"$match": {"isActive": True}},  # Filter to include only active entries
        {"$group": {"_id": "$fuelType", "count": {"$sum": 1}}},  # Group by fuelType and count
        {"$sort": {"count": -1}},  # Sort by count in descending order
        {"$limit": 1}  # Limit to the top result
    ]

    most_frequent_fuelType = list(collection.aggregate(pipeline))

    if most_frequent_fuelType:
        fuelType_name = most_frequent_fuelType[0]['_id']
        fuelType_count = format(most_frequent_fuelType[0]['count'], ',')
    else:
        fuelType_name = "None"
        fuelType_count = 0

    # Displaying in Streamlit
    st.markdown(f"Most frequent active fuel type: **{fuelType_name}** (Count: **{fuelType_count}**)")
    st.markdown("-------------------------------------------------------------------------------")