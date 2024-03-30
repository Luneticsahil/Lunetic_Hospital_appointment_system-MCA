document.addEventListener("DOMContentLoaded", function () {
    const specializationSelect = document.getElementById("specialization");
    const doctorNameSelect = document.getElementById("doctorName");
    const appointmentSlotSelect = document.getElementById("appointmentSlot");

    const doctorNames = {
        "Allergy and immunology": ["Dr. Vijay Kumar", "Dr. Manish", "Dr. Pankaj Sharma"],
        "Anesthesiology": ["Dr. Rahul Kumar", "Dr. Abhishek Singh", "Dr. Shivani Singh"],
        "Dermatology": ["Dr. Arti Mishra", "Dr. Shashank Singh", "Dr. Saurabh Pandey"],
        "Orthopedics": ["Dr. Sanjay Gupta", "Dr. Ritu Sharma", "Dr. Vikram Singh"],
         "Internal Medicine": ["Dr. Meena Patel", "Dr. Mohan Kumar", "Dr. Nisha Gupta"],
            "Obstetrics and Gynecology": ["Dr. Anjali Sharma", "Dr. Sameer Singh", "Dr. Priya Patel"],
            "Pediatrics": ["Dr. Anoop Verma", "Dr. Neha Kapoor", "Dr. Rajesh Gupta"],
            "Radiology": ["Dr. Alok Jain", "Dr. Renuka Singh", "Dr. Ajay Mehta"],
            "General Surgery": ["Dr. Vivek Sharma", "Dr. Pooja Singh", "Dr. Rajiv Gupta"],
            "Ophthalmology": ["Dr. Rakesh Kumar", "Dr. Sunita Sharma", "Dr. Arjun Singh"],
            "ENT": ["Dr. Naveen Verma", "Dr. Shalini Gupta", "Dr. Abhinav Singh"]
        // Add doctor names for other specializations here
    };

    specializationSelect.addEventListener("change", function () {
        const selectedSpecialization = specializationSelect.value;
        const doctors = doctorNames[selectedSpecialization] || [];

        doctorNameSelect.innerHTML = '<option value="" disabled selected>Select Doctor</option>';
        appointmentSlotSelect.innerHTML = '<option value="" disabled selected>Select Time Slot</option>';

        if (doctors.length === 0) {
            doctorNameSelect.innerHTML += '<option value="" disabled>No doctors available for this specialization</option>';
        } else {
            doctors.forEach((doctor) => {
                const option = document.createElement("option");
                option.value = doctor;
                option.textContent = doctor;
                doctorNameSelect.appendChild(option);
            });

            // You can add code here to dynamically generate time slots based on your requirements
        }
    });

    doctorNameSelect.addEventListener("change", function () {
        // You can add code here to dynamically generate time slots based on the selected doctor
        // For now, let's simulate some time slots
        const timeSlots = ["10:00 AM", "11:00 AM", "2:00 PM", "3:00 PM"];

        appointmentSlotSelect.innerHTML = '<option value="" disabled selected>Select Time Slot</option>';

        timeSlots.forEach((timeSlot) => {
            const option = document.createElement("option");
            option.value = timeSlot;
            option.textContent = timeSlot;
            appointmentSlotSelect.appendChild(option);
        });
    });
});


