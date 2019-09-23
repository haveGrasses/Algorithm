def camelToDashLine0(s):
    """lossEntropy可转换为 loss_entropy， someLSTMPre转换为some_lstm_pre"""
    res = ''
    for i in range(len(s)-1):
        if i > 0 and s[i] != s[i].lower() and s[i+1] == s[i+1].lower():
            res += '_'
        elif i > 0 and s[i-1] == s[i-1].lower() and s[i] != s[i].lower():
            res += '_'
        res += s[i].lower()
    res += s[-1].lower() if s[-1] == s[-1].lower() or s[-2] != s[-2].lower() else '_' + s[-1].lower()
    return res


def camelToDashLine(s):
    """lossEntropy可转换为 loss_entropy， someLSTMPre转换为some_lstm_pre
    找到需要加下划线的字母位置:
        1. 该位置不在第一个：i in range(1, len(s))，去头
        1. 该位置是大写
        2. 该位置前面有小些或者后面有小写，判断后有小写的时候注意i不要越界才去判断
    """
    res = s[0].lower()
    for i in range(1, len(s)):
        if s[i] != s[i].lower() and ((i != len(s) - 1 and s[i+1] == s[i+1].lower()) or s[i-1] == s[i-1].lower()):
            res += '_'
        res += s[i].lower()
    return res


test_cases = ['lossEntropy', 'LossEntropy', 'ABLossEntropy', 'ABCLossEntropy', 'lossEntropyA', 'someLSTMPre', 'someLSTM']

for i in test_cases:
    print(camelToDashLine(i))

# loss_entropy
# loss_entropy
# ab_loss_entropy
# loss_entropy_a
# some_lstm_pre
# some_lstm
