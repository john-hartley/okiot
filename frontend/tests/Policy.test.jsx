import { afterEach, expect, test } from "vitest";
import { cleanup, render, screen } from "@testing-library/react";
import Policy from "../src/Policy";

afterEach(() => cleanup());

test("policy details not shown when no policy supplied", () => {
    const policy = null;

    render(<Policy policy={policy} />);

    expect(screen.queryByText("Policy Details")).toBeNull();
});

test("policy details shown when policy supplied", () => {
    const policy = {
        id: 478,
        policyHolder: {
            firstName: "Bugs",
            lastName: "Bunny"
        },
        type: "carrot",
        startsAt: "1999-01-01 00:00:00",
        endsAt: "2028-01-01 00:00:00",
        autoRenews: true
    };

    const actual = render(<Policy policy={policy} />);
    const autoRenewalCheckbox = actual.container.querySelector("#auto-renews");

    expect(screen.getByText("Policy Details")).toBeInTheDocument();
    expect(screen.getByText("478")).toBeInTheDocument();
    expect(screen.getByText("Bugs")).toBeInTheDocument();
    expect(screen.getByText("Bunny")).toBeInTheDocument();
    expect(screen.getByText("carrot")).toBeInTheDocument();
    expect(screen.getByText("1999-01-01 00:00:00")).toBeInTheDocument();
    expect(screen.getByText("2028-01-01 00:00:00")).toBeInTheDocument();
    expect(autoRenewalCheckbox).toBeChecked();
});

test.each([
    [true, true],
    [false, false]
])("auto renewal checked state matches value", (autoRenews, expected) => {
    const policy = {
        id: 999,
        policyHolder: {
            firstName: "N/A",
            lastName: "N/A"
        },
        type: "N/A",
        startsAt: "N/A",
        endsAt: "N/A",
        autoRenews: autoRenews
    };

    const actual = render(<Policy policy={policy} />);
    const autoRenewalCheckbox = actual.container.querySelector("#auto-renews");

    expect(autoRenewalCheckbox.checked).toBe(expected);
});