# Lannister
## Database
### Tables

<details id="users" open="true">
<summary><b>users</b></summary>
<table>
<tr>
<th>Field</th>
<th>Data type</th>
<th>Description</th>
</tr>
<tr>
<td><b>id</b></td>
<td>character(12)</td>
<td>Slack Member ID. A unique primary key.</td>
</tr>
<tr>
<td><b>name</b></td>
<td>character(80)</td>
<td>Slack username.</td>
</tr>
<tr>
<td><b>email</b></td>
<td>character(40)</td>
<td>User email from Slack.</td>
</tr>
<tr>
<td><b>roles</b></td>
<td>user_role[]</td>
<td>List of user roles. Contains one or more roles from <i><a href="#user_role">user_role</a></i> enumerable type.</td>
</tr>
</table>
</details>

<details id="requests">
<summary><b>requests</b></summary>
<table>
<tr>
<th>Field</th>
<th>Data Type</th>
<th>Nullable</th>
<th>Default</th>
<th>References</th>
<th>Description</th>
</tr>
<tr>
<td><b>id</b></td>
<td>int</td>
<td></td>
<td>Next value</td>
<td></td>
<td>Request primary key. Used to uniquely identify each request.</td>
</tr>
<tr>
<td><b>creator</b></td>
<td>character(12)</td>
<td></td>
<td></td>
<td><a href="#users">users</a>.id</td>
<td>The request creator.</td>
</tr>
<tr>
<td><b>reviewer</b></td>
<td>character(12)</td>
<td></td>
<td></td>
<td><a href="#users">users</a>.id</td>
<td>The request reviewer.</td>
</tr>
<tr>
<td><b>bonus_type</b></td>
<td>character(40)</td>
<td></td>
<td></td>
<td></td>
<td>A type of bonus requested by user(overtime, referral bonus, etc.)</td>
</tr>
<tr>
<td><b>description</b></td>
<td>text</td>
<td>null</td>
<td>null</td>
<td></td>
<td>An additional information about the request written by user.</td>
</tr>
<tr>
<td><b>status</b></td>
<td>request_status</td>
<td></td>
<td>created</td>
<td></td>
<td>The request status. Contains one of the options from <i><a href="#request_status">request_status</a></i> enumerable type.</td>
</tr>
<tr>
<td><b>date_created</b></td>
<td>timestamp</td>
<td></td>
<td>Time of creation</td>
<td></td>
<td>Full request creation date. Completes automatically when the request is created.</td>
</tr>
<tr>
<td><b>date_changed</b></td>
<td>timestamp</td>
<td></td>
<td>Time of creation</td>
<td></td>
<td>Full date of the last request change. Completes automatically when the request information is changed.</td>
</tr>
<tr>
<td><b>date_payment</b></td>
<td>timestamp</td>
<td></td>
<td>null</td>
<td></td>
<td>Full date of the payday.</td>
</tr>
</table>

<h4>Constraints:</h4>
    <ul>
        <li>Reviewer must have 'reviewer' role in his <i><a href="#users">users</a>.roles</i> list.</li>
        <li>Creator and reviewer columns cannot reference the same <i><a href="#users">users</a>.id</i>.
    </ul>
</details>

<hr/>

### Enumerable types
<details id="user_role" open="true">
    <summary><b>user_role</b></summary>
    <table style="float: none;">
        <tr><th>Role</th></tr>
        <tr><td>worker</td></tr>
        <tr><td>reviewer</td></tr>
        <tr><td>admin</td></tr>
    </table>
</details>

<details id="request_status">
    <summary><b>request_status</b></summary>
    <table>
        <tr><th>Status</th></tr>
        <tr><td>created</td></tr>
        <tr><td>approved</td></tr>
        <tr><td>rejected</td></tr>
        <tr><td>done</td></tr>
    </table>
</details>

<hr/>


### Database diagram
<div style="float: footnote;"><img src="https://i.ibb.co/BPtvwhQ/2022-06-30-194653600.png"/></div>