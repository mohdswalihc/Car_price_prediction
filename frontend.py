import streamlit as st
import requests

API_URL = "http://0.0.0.0:8000/predict"

st.title("Car prise predictor")

st.markdown('Enter your details below: ')

# input field
Make=st.selectbox("Make",['BMW', 'Audi', 'FIAT', 'Mercedes-Benz', 'Chrysler', 'Nissan',
       'Volvo', 'Mazda', 'Mitsubishi', 'Ferrari', 'Alfa Romeo', 'Toyota',
       'McLaren', 'Maybach', 'Pontiac', 'Porsche', 'Saab', 'GMC',
       'Hyundai', 'Plymouth', 'Honda', 'Oldsmobile', 'Suzuki', 'Ford',
       'Cadillac', 'Kia', 'Bentley', 'Chevrolet', 'Dodge', 'Lamborghini',
       'Lincoln', 'Subaru', 'Volkswagen', 'Spyker', 'Buick', 'Acura',
       'Rolls-Royce', 'Maserati', 'Lexus', 'Aston Martin', 'Land Rover',
       'Lotus', 'Infiniti', 'Scion', 'Genesis', 'HUMMER', 'Tesla',
       'Bugatti'])

Year=st.number_input("Year",min_value=1990,max_value=2017,value=2010)

Engine_Fuel_Type = st.selectbox(
    "Engine fuel type",
    [
        'premium unleaded (required)', 
        'regular unleaded',
        'premium unleaded (recommended)', 
        'flex-fuel (unleaded/E85)',
        'diesel', 
        'electric',
        'flex-fuel (premium unleaded recommended/E85)', 
        'natural gas',
        'flex-fuel (premium unleaded required/E85)',
        'flex-fuel (unleaded/natural gas)'
    ],index=5)

Engine_HP=st.number_input("Engine HP",min_value=55.,max_value=1001.,value=200.,step=10.)

Engine_Cylinders=st.number_input("Engine_Cylinders",max_value=16.,min_value=1.,step=1.,value=2.)

Transmission_Type=st.selectbox('Transmission Type',['MANUAL', 'AUTOMATIC',  'AUTOMATED_MANUAL', 'DIRECT_DRIVE'])

Driven_Wheels=st.selectbox("Driven Wheels",['rear wheel drive', 'front wheel drive', 'all wheel drive','four wheel drive'])

Number_of_Doors=st.number_input('Number of Doors',max_value=4,min_value=2,value=4)

Market_Category=st.selectbox(
       'Market Category',
    [  'Factory Tuner,Luxury,High-Performance', 'Luxury,Performance',
       'Luxury,High-Performance', 'Luxury', 'Performance', 'Flex Fuel',
       'Flex Fuel,Performance', 'Hatchback',
       'Hatchback,Luxury,Performance', 'Hatchback,Luxury',
       'Luxury,High-Performance,Hybrid', 'Diesel,Luxury',
       'Hatchback,Performance', 'Hatchback,Factory Tuner,Performance',
       'High-Performance', 'Factory Tuner,High-Performance',
       'Exotic,High-Performance', 'Exotic,Factory Tuner,High-Performance',
       'Factory Tuner,Performance', 'Crossover', 'Exotic,Luxury',
       'Exotic,Luxury,High-Performance', 'Exotic,Luxury,Performance',
       'Factory Tuner,Luxury,Performance', 'Flex Fuel,Luxury',
       'Crossover,Luxury', 'Hatchback,Factory Tuner,Luxury,Performance',
       'Crossover,Hatchback', 'Hybrid', 'Luxury,Performance,Hybrid',
       'Crossover,Luxury,Performance,Hybrid',
       'Crossover,Luxury,Performance',
       'Exotic,Factory Tuner,Luxury,High-Performance',
       'Flex Fuel,Luxury,High-Performance', 'Crossover,Flex Fuel',
       'Diesel', 'Hatchback,Diesel', 'Crossover,Luxury,Diesel',
       'Crossover,Luxury,High-Performance',
       'Exotic,Flex Fuel,Factory Tuner,Luxury,High-Performance',
       'Exotic,Flex Fuel,Luxury,High-Performance',
       'Exotic,Factory Tuner,Luxury,Performance', 'Hatchback,Hybrid',
       'Crossover,Hybrid', 'Hatchback,Luxury,Hybrid',
       'Flex Fuel,Luxury,Performance', 'Crossover,Performance',
       'Luxury,Hybrid', 'Crossover,Flex Fuel,Luxury,Performance',
       'Crossover,Flex Fuel,Luxury', 'Crossover,Flex Fuel,Performance',
       'Hatchback,Factory Tuner,High-Performance', 'Hatchback,Flex Fuel',
       'Factory Tuner,Luxury',
       'Crossover,Factory Tuner,Luxury,High-Performance',
       'Crossover,Factory Tuner,Luxury,Performance',
       'Crossover,Hatchback,Factory Tuner,Performance',
       'Crossover,Hatchback,Performance', 'Flex Fuel,Hybrid',
       'Flex Fuel,Performance,Hybrid',
       'Crossover,Exotic,Luxury,High-Performance',
       'Crossover,Exotic,Luxury,Performance', 'Exotic,Performance',
       'Exotic,Luxury,High-Performance,Hybrid', 'Crossover,Luxury,Hybrid',
       'Flex Fuel,Factory Tuner,Luxury,High-Performance',
       'Performance,Hybrid', 'Crossover,Factory Tuner,Performance',
       'Crossover,Diesel', 'Flex Fuel,Diesel',
       'Crossover,Hatchback,Luxury'],index=3)

Vehicle_Size=st.selectbox(
       'Vehicle Size',
       ['Compact', 'Midsize', 'Large'])

Vehicle_Style=st.selectbox(
       'Vehicle Style',
       ['Coupe', 'Convertible', 'Sedan', 'Wagon', '4dr Hatchback',
       '2dr Hatchback', '4dr SUV', 'Passenger Minivan', 'Cargo Minivan',
       'Crew Cab Pickup', 'Regular Cab Pickup', 'Extended Cab Pickup',
       '2dr SUV', 'Cargo Van', 'Convertible SUV', 'Passenger Van'])

highway_MPG=st.number_input('highway MPG',max_value=100 ,min_value=12,value=30)

city_mpg=st.number_input('city mpg',max_value=135 ,min_value=7 ,value= 25)

Popularity=st.number_input('Popularity',max_value=5500,min_value= 10,value=1000)


if st.button("Predict the Price"):

    input_data = {
        "Make": Make,
        "Year": Year,
        "Engine Fuel Type": Engine_Fuel_Type,
        "Engine HP": Engine_HP,
        "Engine Cylinders": Engine_Cylinders,
        "Transmission Type": Transmission_Type,
        "Driven_Wheels": Driven_Wheels,
        "Number of Doors": Number_of_Doors,
        "Market Category": Market_Category,
        "Vehicle Size": Vehicle_Size,
        "Vehicle Style": Vehicle_Style,
        "highway MPG": highway_MPG,
        "city mpg": city_mpg,
        "Popularity": Popularity
    }

    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        price = response.json()["predicted_price_is"]
        st.success(f"Estimated Car Price: $ {price:,.2f}")
    else:
        st.error("Prediction failed")



















