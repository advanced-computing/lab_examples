from flask import Flask, jsonify, request
import pandas as pd 

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World!</p>"


@app.get("/api/list")
def list():
    format = request.args.get('format', 'json')
    filterby = request.args.get('filterby',None)
    filtervalue = request.args.get('filtervalue',None)
    limit = int(request.args.get('limit', 1000))
    offset = int(request.args.get('offset', 0))

    data = pd.read_csv('videos_data.csv')
    if filterby:
        if filtervalue is None:
            return "Invalid filtervalue"
        elif filterby not in data.columns:
            return "Invalid filterby column"
        else:
            data = data[data[filterby] == int(filtervalue)]
    data = data.iloc[offset:offset+limit]
    if format == 'json':
        return jsonify(data.to_dict(orient='records'))
    elif format == 'csv':
        return data.to_csv(index=False)
    else:
        return "Invalid format"

if __name__ == "__main__":
    app.run(debug=True)