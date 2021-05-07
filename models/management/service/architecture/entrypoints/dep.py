# ------------------------------------ Batches ------------------------------------------
@app.route("/batches", methods = [ 'GET' ]) 
def batches():
    print('*** batches')
    batches = get_all_batches()
    return jsonify([batch.to_json() for batch in batches]), 201 

def get_all_batches():
    batches = []
    arr = [
            ('Red Table', 'batch-1', 1, None),
            ('Blue Table', 'batch-2', 2, None),
            ('Green Table', 'batch-3', 3, None)
    ]
    for data in arr:
        batch = model.Batch(data[0], data[1], data[2], data[3])
        batches.append(batch)
    return batches 

