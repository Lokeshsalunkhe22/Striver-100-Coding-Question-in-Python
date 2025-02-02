def can_save_patients(vaccine_strengths, patient_counts):
    vaccine_strengths.sort()
    patient_counts.sort()
    
    for i in range(len(patient_counts)):
        if vaccine_strengths[i] < patient_counts[i]:
            return "No"  
    return "Yes" 

if __name__ == "__main__":
    t = int(input())
    vacancies = int(input())
    vaccine_strengths = list(map(int, input().split()))
    patient_counts = list(map(int, input().split()))

    print(can_save_patients(vaccine_strengths, patient_counts))