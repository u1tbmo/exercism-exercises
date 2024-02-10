#include "grade_school.h"

// Initialize a Roster
bool init_roster(roster_t *roster)
{
    // Initialize roster count to 0
    roster->count = 0;

    return true;
}

// Add student to school roster
bool add_student(roster_t *roster, char *name, uint8_t grade)
{
    // Initialize a student
    student_t student;
    student.grade = grade;
    strcpy(student.name, name);

    // Check if the student is a duplicate
    if (is_duplicate(roster, student))
    {
        return false;
    }

    // Add the student to the roster
    roster->students[roster->count] = student;
    roster->count++;

    // Sort the students in the roster
    qsort(roster->students, roster->count, sizeof(student_t), comparator);

    return true;
}

roster_t get_grade(roster_t *roster, uint8_t grade)
{
    // Initialize a new roster
    roster_t grade_roster;
    init_roster(&grade_roster);

    // Iterate over all students in the roster
    for (size_t i = 0; i < roster->count; i++)
    {
        // If the student's grade matches the input grade received by the function, add them to the roster.
        if (roster->students[i].grade == grade)
        {
            add_student(&grade_roster, roster->students[i].name, grade);
        }
    }

    // Return the grade roster
    return grade_roster;
}

bool is_duplicate(roster_t *roster, student_t student)
{
    for (uint8_t i = 0; i < roster->count; i++)
    {
        if (strcmp(student.name, roster->students[i].name) == 0)
        {
            return true;
        }
    }
    return false;
}

// Comparator function for qsort
int comparator(const void *x_void, const void *y_void)
{
    // Cast the void pointers to student_t pointers
    student_t s1 = *(student_t *)x_void;
    student_t s2 = *(student_t *)y_void;

    // Sort by grade
    if (s1.grade != s2.grade)
    {
        return s1.grade - s2.grade;
    }
    else
    {
        // Sort by name if grades are equal
        return strcmp(s1.name, s2.name);
    }
}