preds = model.predict_classes(x_test)

    inst = 0
    totest = preds.shape[0]
    for i in range(totest):
        if preds[i] != y_testz[i]:
            inst += 1
    inst2 = totest - inst
    print inst, inst2, inst + inst2
    mis_ins = np.zeros((inst, 100, 100, 3))
    mins = np.zeros((inst, 2)).astype('int')
    cor_ins = np.zeros((inst2, 100, 100, 3))
    cins = np.zeros((inst2, 2)).astype('int')
    i, k = 0, 0
    for l in range(totest):
        if preds[l] == y_testz[l]:
            cor_ins[k, :, :, :] = x_test[l, :, :, :]
            cins [k, 0] = preds[l]
            cins [k, 1] = y_testz[l]
            k +=1

        if preds[l] != y_testz[l]:
            mis_ins[i, :, :, :] = x_test[l, :, :, :]
            mins[i, 0] = preds[l]
            mins[i, 1] = y_testz[l]
            i +=1

    print mis_ins.shape, cor_ins.shape
    
    def plot_activations (ins, layer, image, no, labs):
    path = 'act/' + str(image) + ' Image '  + str(no) + ' ' + ' Label: ' + str(labs[0]) + ' Predicted:' + str(labs[1]) + ' Activation Layer ' + str(layer) + '.png'
    name = str(image) + ' Image '  + str(no) + ' ' + ' Label: ' + str(labs[0]) + ' Predicted:' + str(labs[1]) + ' Activation Layer ' + str(layer)
    l = ins.shape[3]
    l2 = np.ceil(math.sqrt(l)).astype('int')
    x, y = l2, l2
    fig = plt.figure()
    plt.title(name)
    plt.axis('off')
    for i in range(l):
        ax = fig.add_subplot(x, y, i+1)
        plt.imshow(ins[0,:,:,i])
        plt.axis('off')
    fig.savefig(path)
    return plt

def plotImages(ins, type):
    path = 'act/' + type + '.png'
    l = ins.shape[0]
    l2 = np.ceil(math.sqrt(l)).astype('int')
    x, y = l2, l2
    fig = plt.figure()
    plt.title(type)
    plt.axis('off')
    for i in range(l):
        ax = fig.add_subplot(x, y, i + 1)
        plt.imshow(ins[i, :, :, :])
        plt.axis('off')
    fig.savefig(path)
    return plt


x = np.zeros((1, 100, 100, 3))

plotImages(mis_ins, 'Miss classified Images')
plotImages(cor_ins, 'Correct Classified Images')

for j in range(inst):
    x[0, :, :, :] = mis_ins[j, :, :, :]
    for i in range(4):
        get_3rd_layer_output = K.function([model.layers[0].input],
                                          [model.layers[i].output])
        layer_output = get_3rd_layer_output([x])[0]
        plot_activations(layer_output, i, 'Miss classified', j+1, mins[j])


for j in range(inst2):
    x[0, :, :, :] = cor_ins[j, :, :, :]
    for i in range(4):
        get_3rd_layer_output = K.function([model.layers[0].input],
                                          [model.layers[i].output])
        layer_output = get_3rd_layer_output([x])[0]
        plot_activations(layer_output, i, 'Correct classified', j+1, cins[j])
