import math


def get_p95(log: list) -> float:
    
    # sort ascending
    log = sorted(log, key = lambda d: d['latency_ms'])
    rank_95_idx =  math.ceil(0.95 * len(log)) - 1 # back to zero idx
    
    return float(log[rank_95_idx]['latency_ms'])
    
def get_agreement_rate(production_log: list, shadow_log: list) -> float:

    match = 0
    num_req = len(production_log)
    
    # assume input_id are already aligned for both logs
    for prod_req, shad_req in zip(production_log, shadow_log):
        if prod_req['prediction'] == shad_req['prediction']:
            match += 1
            
    return float(match/num_req)

def get_acc(log: list) -> float:

    correct = 0
    num_req = len(log)
    for request in log:
        if request['actual'] == request['prediction']:
            correct += 1
            
    return float(correct/num_req)

    
def evaluate_shadow(production_log: list, shadow_log: list, criteria: dict) -> dict:
    """
    Returns a dictionary with the promotion decision and metrics.
    """

    isPromote = False
    shadow_accuracy = get_acc(shadow_log)
    production_accuracy = get_acc(production_log)
    accuracy_gain = shadow_accuracy - production_accuracy

    agreement_rate = get_agreement_rate(production_log, shadow_log)
    shadow_latency_p95 = get_p95(shadow_log)

    if accuracy_gain >= criteria['min_accuracy_gain'] and agreement_rate >= criteria['min_agreement_rate'] and shadow_latency_p95 <= criteria['max_latency_p95']:
        isPromote = True


    return {"promote": isPromote, 
            "metrics": {"shadow_accuracy" : shadow_accuracy, 
                        "production_accuracy" : production_accuracy, 
                        "accuracy_gain" : accuracy_gain,
                        "shadow_latency_p95" : shadow_latency_p95,
                        "agreement_rate" : agreement_rate
                        }
           }
