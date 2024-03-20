def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    num_students = 5
    subjects = ['C언어', '영어', '파이썬']
    students = []

    # 학생 정보 입력 받기
    for i in range(num_students):
        name = input(f"학생 {i+1}의 이름을 입력하세요: ")
        scores = []
        for subject in subjects:
            score = float(input(f"{name} 학생의 {subject} 점수를 입력하세요: "))
            scores.append(score)
        total_score = sum(scores)
        students.append({'name': name, 'scores': scores, 'total_score': total_score})

    # 총점을 기준으로 학생들을 정렬하여 등수를 부여
    students.sort(key=lambda x: x['total_score'], reverse=True)
    for i, student in enumerate(students):
        student['rank'] = i + 1

    # 각 학생의 총점, 평균, 학점, 등수를 출력
    print("\n===== 학생 성적표 =====")
    for student in students:
        total_score = student['total_score']
        average_score = total_score / len(subjects)
        grade = calculate_grade(average_score)
        print(f"{student['name']} 학생의 총점: {total_score}, 평균: {average_score:.2f}, 학점: {grade}, 등수: {student['rank']}등")

if __name__ == "__main__":
    main()
