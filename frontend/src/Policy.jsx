const Policy = ({ policy }) => {
    if (!policy) {
        return;
    }

    return (
        <>
            <h2>Policy Details</h2>

            <table>
                <tbody>
                    <tr>
                        <td>Id</td>
                        <td>{policy.id}</td>
                    </tr>
                    <tr>
                        <td>First name</td>
                        <td>{policy.policyHolder.firstName}</td>
                    </tr>
                    <tr>
                        <td>Last name</td>
                        <td>{policy.policyHolder.lastName}</td>
                    </tr>
                    <tr>
                        <td>Policy Type</td>
                        <td>{policy.type}</td>
                    </tr>
                    <tr>
                        <td>Starts at</td>
                        <td>{policy.startsAt}</td>
                    </tr>
                    <tr>
                        <td>Ends at</td>
                        <td>{policy.endsAt}</td>
                    </tr>
                    <tr>
                        <td>Auto renews</td>
                        <td><input id="auto-renews" type="checkbox" checked={policy.autoRenews} readOnly /></td>
                    </tr>
                </tbody>
            </table>
        </>
    );
}

export default Policy;