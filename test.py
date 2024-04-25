
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



import streamlit as st


# Input fields for numbers
num1 = st.number_input('Enter first number', value=0)
num2 = st.number_input('Enter second number', value=0)


operation = st.selectbox('Choose an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])


def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2 if num2 != 0 else 'Cannot divide by zero'

if st.button('Result'):
    result = calculate(num1, num2, operation)
    st.write('The result is:', result)