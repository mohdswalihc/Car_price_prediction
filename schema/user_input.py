# creating a pidantic model to validate incoming data

from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Annotated,Literal,Optional

class UserInput(BaseModel):


    Make: Annotated[
    str,
    Field(..., description="enter a valid make")
    ]
    
    Year:Annotated[int,Field(...,gt=1989,lt=2018,description='enter the year between 1990 -2017')]

    Engine_Fuel_Type:Annotated[Literal['premium unleaded (required)', 'regular unleaded',
       'premium unleaded (recommended)', 'flex-fuel (unleaded/E85)',
       'diesel', 'electric',
       'flex-fuel (premium unleaded recommended/E85)', 'natural gas',
       'flex-fuel (premium unleaded required/E85)',
       'flex-fuel (unleaded/natural gas)'],Field(...,alias='Engine Fuel Type',description="enter is a diesel or electric")]
    
    Engine_HP:Annotated[float,Field(...,gt=54,lt=1001,description='enter the engine hp',alias='Engine HP')]

    Engine_Cylinders:Annotated[float,Field(...,alias='Engine Cylinders',gt=0,lt=17,description='enter the engine cylider bet ween 1-16')]

    TransmissionType:Annotated[Literal['MANUAL', 'AUTOMATIC', 'AUTOMATED_MANUAL', 'DIRECT_DRIVE'],Field(...,description='enter what you want from these',alias="Transmission Type")]

    Driven_Wheels:Annotated[Literal['rear wheel drive', 'front wheel drive', 'all wheel drive','four wheel drive'],Field(...,description='enter the ttype from =rear wheel drive, front wheel drive, all wheel drive,four wheel drive')]

    Number_of_Doors:Annotated[float,Field(...,gt=1,lt=5,description='enter the number of doors you want',alias='Number of Doors')]

    Market_Category: Annotated[
    str,
    Field(..., alias="Market Category", description="select from Market Category list")
    ]

    Vehicle_Size:Annotated[Literal['Compact', 'Midsize', 'Large'],Field(...,description='select Compact or Midsize or  Large',alias='Vehicle Size')]
    
    ##
    
    Vehicle_Style:Annotated[Literal['Coupe', 'Convertible', 'Sedan', 'Wagon', '4dr Hatchback','2dr Hatchback', '4dr SUV', 'Passenger Minivan', 'Cargo Minivan','Crew Cab Pickup', 'Regular Cab Pickup', 'Extended Cab Pickup','2dr SUV', 'Cargo Van', 'Convertible SUV', 'Passenger Van'],Field(...,alias='Vehicle Style',description=f'select from - Coupe, Convertible, Sedan,Wagon')]

    highway_MPG:Annotated[int,Field(...,alias='highway MPG',gt=12,lt=355)]

    city_mpg:Annotated[int,Field(...,alias='city mpg',description='enter the between 5-135',gt=6,lt=138,)]

    Popularity:Annotated[int,Field(...,description='enter the number between 1-5000',gt=1,lt=5500)]

    @field_validator('Vehicle_Style', mode="before")
    @classmethod
    def normalize_city(cls,v :str)-> str:
        v=v.strip().title()
        return v
    

    @field_validator('Make','TransmissionType',mode='before')
    @classmethod
    def cappitalize(cls,v :str)->str:
        v=v.strip().upper()
        return v
