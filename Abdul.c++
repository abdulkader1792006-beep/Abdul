#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Subject {
public:
    string name;
    float studyHours;
    float marks;

    Subject(string n, float h, float m) {
        name = n;
        studyHours = h;
        marks = m;
    }
};

int main() {
    int n;
    cout << "Enter number of subjects: ";
    cin >> n;

    vector<Subject> subjects;

    for(int i = 0; i < n; i++) {
        string name;
        float hours, marks;

        cout << "\nSubject " << i+1 << " name: ";
        cin >> name;

        cout << "Study hours: ";
        cin >> hours;

        cout << "Marks obtained: ";
        cin >> marks;

        subjects.push_back(Subject(name, hours, marks));
    }

    float totalMarks = 0;
    float totalHours = 0;

    cout << "\n--- Study Summary ---\n";
    for(auto s : subjects) {
        cout << "Subject: " << s.name 
             << ", Study Hours: " << s.studyHours 
             << ", Marks: " << s.marks << endl;

        totalMarks += s.marks;
        totalHours += s.studyHours;
    }

    float average = totalMarks / n;

    cout << "\nTotal Study Hours: " << totalHours << endl;
    cout << "Average Marks: " << average << endl;

    // Performance Suggestion
    if(average >= 85)
        cout << "Performance: Excellent 🎯" << endl;
    else if(average >= 70)
        cout << "Performance: Good 👍" << endl;
    else if(average >= 50)
        cout << "Performance: Average ⚠" << endl;
    else
        cout << "Performance: Needs Improvement ❗" << endl;

    return 0;
}
