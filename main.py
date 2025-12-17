def main():
    errors = []
    valid_results = []
    fail_counts = {}

    print("Enter testName and status (comma-separated).")
    print("Press Enter on an empty line to finish.\n")

    while True:
        user_input = input()
        if not user_input.strip():
            break

        # If a Missing comma
        if "," not in user_input:
            errors.append(user_input)
            continue

        test_name, status = [item.strip() for item in user_input.split(",", 1)]

        # Empty test name
        if not test_name:
            errors.append(user_input)
            continue

        # Normalize and validate status
        status_normalized = status.strip().upper()
        if status_normalized not in ("PASS", "FAIL"):
            errors.append(user_input)
            continue

        # Valid input
        valid_results.append({
            "testName": test_name,
            "status": status_normalized
        })

        # Track fail counts
        if status_normalized == "FAIL":
            fail_counts[test_name] = fail_counts.get(test_name, 0) + 1

    # Summary
    total_valid = len(valid_results)
    pass_count = sum(1 for r in valid_results if r["status"] == "PASS")
    fail_count = sum(1 for r in valid_results if r["status"] == "FAIL")
    invalid_count = len(errors)

    if fail_counts:
        max_fails = max(fail_counts.values())

        tied_tests = [
            test for test, count in fail_counts.items() if count == max_fails
        ]

        top_failing_test = min(
            tied_tests,
            key=lambda t: t[0].lower()
        )
    else:
        top_failing_test = None

    # Output
    print("\nValid Results:")
    for i, result in enumerate(valid_results, start=1):
        print(f"{i}. Test Name: {result['testName']}, Status: {result['status']}")

    print("\nSummary:")
    print(f"Total Valid   : {total_valid}")
    print(f"Pass Count   : {pass_count}")
    print(f"Fail Count   : {fail_count}")
    print(f"Invalid Count: {invalid_count}")
    print(f"Top Failing Test: {top_failing_test}")

    print("\nInvalid Inputs:")
    for err in errors:
        print(err)


if __name__ == "__main__":
    main()