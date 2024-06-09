def f1_score_eval_model(tp, fp, fn):
    # Check data type
    if type(tp) != int:
        print("tp must be int")
        return
    if type(fp) != int:
        print("fp must be int")
        return
    if type(fn) != int:
        print("fn must be int")
        return
    
    # Check >0
    if tp <= 0 or fp <= 0 or fn <=  0:
        print("tp and fp and fn must be greater than zero")
        return
    
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1_score = 2*(precision * recall)/(precision + recall)

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')

# f1_score_eval_model(tp=2, fp=3, fn=4)
# f1_score_eval_model(tp='a', fp=3, fn=4)
# f1_score_eval_model(tp=2, fp ='a', fn=4)
# f1_score_eval_model(tp=2, fp =3, fn='a')
# f1_score_eval_model(tp=2, fp =3, fn=0)
# f1_score_eval_model(tp=2.1, fp =3, fn=0)