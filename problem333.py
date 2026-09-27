notes = {
    500: 10,
    200: 15,
    100: 20
}

withdraw = 4300
remaining = withdraw

for note in sorted(notes.keys(), reverse=True):
    required = remaining // note
    used = min(required, notes[note])

    remaining -= used * note
    notes[note] -= used

    if used > 0:
        print(note, "×", used)

if remaining == 0:
    print("Withdrawal successful")
else:
    print("Unable to provide exact amount")