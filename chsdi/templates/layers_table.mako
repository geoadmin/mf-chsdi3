<!DOCTYPE html>
<html>
<head>
  <title>Layers Table</title>
  <style>
    table {
      border-collapse: collapse;
      width: 100%;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    th {
      background-color: #f2f2f2;
      font-weight: bold;
    }
    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
    tr:hover {
      background-color: #e9e9e9;
    }
  </style>
</head>
<body>
  <h1>Layers Configuration Table</h1>
  <table>
    <thead>
      <tr>
        <th>Technical Name</th>
        <th>Official Name</th>
        <th>Layer Type</th>
        <th>Has Tooltip</th>
        <th>Is Searchable</th>
      </tr>
    </thead>
    <tbody>
      % for layer_id, layer_config in layers.items():
        <tr>
          <td>${layer_config.get('serverLayerName', '-')}</td>
          <td>${layer_config.get('label', '-')}</td>
          <td>${layer_config.get('type', '-')}</td>
          <td>${'Yes' if layer_config.get('tooltip', False) else 'No'}</td>
          <td>${'Yes' if layer_config.get('searchable', False) else 'No'}</td>
        </tr>
      % endfor
    </tbody>
  </table>
</body>
</html>
