==========================
DASHBOARD-PRODUCTION APIs
==========================
/appointments/

* payment api for appointments
Methods : ['POST', 'OPTIONS']
Endpoint : /appointment_pay/<payment_gateway>
New Endpoint : /appointments/payments/<payment_gateway>
Request params : 
    {
        'payment_gateway': 'payment-gateway-name'
    }

* payment status update
Methods : ['POST', 'OPTIONS']
Endpoint : /updatePaymentStatusByPilot

New Method : ['PATCH', 'PUT'])
New Endpoint : /appointments/payments/

Notes : update payment status
params : {'slot_id':'}


* appointment payment callback
Methods : ['POST', 'OPTIONS']
Endpoint : /appointment_callback/<payment_gateway>
New Endpoint : /appointment/payments/<payment_gateway>/callback/


* fetch inactive dates
Methods : ['POST', 'GET']
Endpoint : /inactiveDates
New Endpoint : appointments/inactive-dates
params : {
    'dates': '',
    'hod_id'
}


Method : ['GET', 'POST', 'OPTIONS']
Endpoint : /getAppoQues
New Endpoint : /appointments/questions/


Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /cancleAppointment
Endpoint : /cancelAppointmentByAdmin
Endpoint : /cancelAppointmentByPilot

New Endpoint : /appointments/<slot-id>/
Description : Should be a patch request
TODO : sendSms service should go in thread
params : {
    'status':'A'
}


Notes : Not in use
Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /getIcalfile


Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /getHodappointmentAddress
New Endpoint : /appointments/address/?hode_code=<hod-code>&hod_status=<hod-status>


Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /viewAppointments
New Endpoint : /appointments/?access_id=''&date=''&access_type=''&hod_code=''
params : {
    'access_id': '', 
    'date': '', 
    'access_type'='P/H', 
    'hod_code'
}


Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /viewAppointmentByMobile
New Endpoint : /appointments/?mobile=''


Endpoint : /confirmHealthCheckStatus
Method : ['GET', 'POST', 'OPTIONS'])
New Endpoint : /appointments/<slot-id>/
Notes : PATCH Request
params : {
    'action_type':''
}


Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /getSlotAvaliability_web1


Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /getTimeSlotsBybuilding
Endpoint : /getTimeSlots1
Endpoint : /v2/get_hods_slots

New Endpoint : /appointments/available-slots/
Notes : Group of station
params : {
    'month_no':'',
    'building_id':'',
}

* can-be-reuse
Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /getTimeSlots1
Endpoint : /appointments/available-slots/
params : {
    'month_no':'',
    'hod_code':'',
}

* can-be-reuse
Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /v2/get_hods_slots
New Endpoint : /appointments/?city_id=''&company_id=''
Notes : data_format --> time/slots/date/area/name/hod_id

* different level shit
Method : ['GET', 'POST', 'OPTIONS'])
Endpoint : /appointments/check_tesco_employee
Notes : HACK GOES HERE

* all together make sense
Method : ['GET', 'OPTIONS'])
Endpoint : /appointments/booked_csv
Endpoint : /appointments/home_health_checks_csv
Endpoint : /appointments/ext/booked_csv
Endpoint : /appointments/ext/home_health_checks_csv

New Endpoint : /appointments/export/?'hod_ids'=''&format=''
params : {
    'hod_ids'='',
    'format':'',
    'report_type':'home_health_check/booked/'

}

Notes : Default format is CSV
