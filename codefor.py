#include <stdio.h>

#define MAX 10

int main() {
    char task[MAX][30];
    int time[MAX];
    int sessions = 0;
    int totalTime = 0;
    int choice;

    do {
        printf("\n=== Productivity & Focus Tracker ===\n");
        printf("1. Add Study Session\n");
        printf("2. View Daily Summary\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1) {
            if (sessions >= MAX) {
                printf("Daily limit reached!\n");
            } else {
                printf("Enter task name: ");
                scanf(" %s", task[sessions]);

                printf("Enter study time (in minutes): ");
                scanf("%d", &time[sessions]);

                totalTime += time[sessions];
                sessions++;

                printf("Study session added!\n");
            }
        }

        else if (choice == 2) {
            printf("\n--- Daily Productivity Summary ---\n");
            for (int i = 0; i < sessions; i++) {
                printf("%d. %s - %d minutes\n", i + 1, task[i], time[i]);
            }
            printf("Total Focus Sessions : %d\n", sessions);
            printf("Total Study Time     : %d minutes\n", totalTime);
        }

        else if (choice == 3) {
            printf("Exiting... Stay focused bro 💪\n");
        }

        else {
            printf("Invalid choice!\n");
        }

    } while (choice != 3);

    return 0;
}