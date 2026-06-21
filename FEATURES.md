# Features Guide

Detailed walkthrough of all features in the To-Do app.

## Calendar View (Month Grid)

### What It Shows
A traditional calendar grid for the current month, showing:
- **Day numbers** (1-31)
- **Task badges** (e.g., `2/3`) showing how many tasks are done vs. total
- **Today's date** highlighted in light purple
- **Past dates** slightly dimmed
- **Other month's dates** (prev/next month overlap) in gray

### Navigation
- Click **`←`** to go to the previous month
- Click **`→`** to go to the next month
- Click **"Go to today"** at the bottom to jump back to today's date

### Clicking a Date
- Click any date to view/add/manage tasks for that day
- The day view page will open

## Day View

### Layout
- **Header:** Date and day name (e.g., "Sunday, June 21, 2026")
- **Add form:** Input box, time picker, and Add button
- **Task list:** All tasks for that day in ascending time order
- **Back link:** "← Back to calendar" to return to month view

### Add a To-Do

1. Type the task name in the text input (e.g., "Buy groceries")
2. (Optional) Click the time field and pick a time (e.g., "14:30")
   - If you leave it empty, it defaults to the current time
3. Click **Add**
4. The task appears in the list below, sorted by time

**Example:**
```
What needs doing?  [Buy groceries  ]  [14:30] [Add]
```

### Task List Display

Each task shows:
- **Square checkbox** (empty or filled with checkmark when done)
- **Time** in light gray (e.g., "14:30")
- **Task title**
- **Date field** (shows the current date, editable)
- **Move button** to reschedule
- **Delete button** (✕) to remove

**Example:**
```
☐  14:30  Buy groceries    06/21/2026  [Move]  [✕]
✓  10:00  Meeting done     06/21/2026  [Move]  [✕]
```

### Mark Complete

Click the **square checkbox** next to a task:
- It fills with a purple checkmark (✓)
- The task text gets a strikethrough
- The count in the calendar updates (e.g., from `1/2` to `2/2`)

Click again to uncheck it.

### Reschedule (Move to Another Date)

1. Change the **date field** next to the task (click the calendar icon)
2. Pick a new date
3. Click **Move**
4. You'll be taken to that date's page, and the task is now there

**Useful for:**
- Moving a task you didn't finish today to tomorrow
- Planning ahead and moving future tasks around
- Re-ordering your week

### Delete

Click the **✕** button to remove a task permanently. It won't be recoverable, so be sure.

## Sorting

Tasks are automatically sorted by **date, then time** in ascending order:
- Earlier dates come first
- Within the same date, earlier times come first

**Example (same day):**
```
08:00  Morning meeting
10:30  Call with client
14:00  Lunch prep
18:00  Evening review
```

If you move a task to a different date, it automatically resorts.

## Viewing Past Tasks

You can browse any month in the past to see what you did:

1. Click **`←`** repeatedly to go back months
2. Days in the past are dimmed to indicate they're in the past
3. Click a past date to see what tasks you had
4. You can still edit or delete past tasks if needed

**Use cases:**
- Review what you accomplished last week
- Check if you completed something you remember
- Find a note or reminder you wrote down earlier

## Viewing Future Tasks

Plan ahead by adding tasks to future dates:

1. Click **`→`** to navigate to future months
2. Click a future date and add tasks
3. The calendar shows task counts so you can see which days are busy
4. Navigate back to today when ready

**Use cases:**
- Plan vacation tasks
- Schedule project milestones
- Prep for busy weeks ahead

## Calendar Badge (Task Count)

Each date with tasks shows a small badge in the bottom-right of the day cell:

- **`1/3`** = 1 task done, 3 total
- **`0/2`** = 0 tasks done, 2 total
- **`2/2`** = All 2 tasks done

**Color coding:**
- Blue background (by default) on the badge

Badges only appear for dates that have at least one task.

## Today Indicator

The current date is highlighted with a **light purple background**. Other dates in the month have a white background.

Click **"Go to today"** at the bottom of the calendar to jump back if you've navigated to past/future months.

## Time Field

Each task has a **time** associated with it:

- Default is the current time (e.g., 14:30 if you add it at 2:30 PM)
- You can set any time (24-hour format: 00:00 to 23:59)
- Tasks sort by time within the same day
- Time is optional — leaving it empty uses the current time

**Why times matter:**
- See your tasks in the order they'll happen
- Schedule your day
- Distinguish between morning, afternoon, evening tasks

## Status Indicators

### Completed Tasks
- Text is **struck through**
- Checkbox is **filled purple with a checkmark**
- Still counts in the calendar badge (e.g., `3/5` = 3 done out of 5)

### Incomplete Tasks
- Text is **normal**
- Checkbox is **empty white square**

## Dark vs. Light Dates

- **Normal date** = Today or a current-month date you haven't reached yet
- **Dimmed date** = In the past
- **Gray date** = From the previous or next month (not clickable per se, but you can click to navigate)

This visual helps you quickly see if a date is in the past or future.

## Tips & Tricks

1. **Quickly add a task for tomorrow:** Navigate to tomorrow's date and add the task
2. **Reschedule multiple times:** You can move a task between dates as often as needed
3. **Review the week:** Click each day to see what you have planned
4. **Mark tasks as you go:** Check them off throughout the day
5. **Look back:** Browse past months to see what you accomplished

## Keyboard Shortcuts

Currently, there are no keyboard shortcuts. Features are accessed via clicking. If you'd like keyboard shortcuts, that can be added in a future update.
