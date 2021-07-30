import ml_collections
import torch


def get_default_configs():
    config = ml_collections.ConfigDict()

    # training
    config.training = training = ml_collections.ConfigDict()
    config.training.batch_size = 8
    training.epochs = 2000
      # Time in epochs
    training.checkpoint_save_freq = 50
    training.sampling_freq = 25
      # Time in steps
    training.log_freq = 50
    training.eval_freq = 5000
    training.snapshot_sampling = True
    training.reduce_mean = False

    # sampling
    config.sampling = sampling = ml_collections.ConfigDict()
    sampling.n_steps_each = 1
    sampling.noise_removal = True
    sampling.probability_flow = False
    sampling.snr = 0.1
    sampling.batch_size = 1
    sampling.sampling_height = 256
    sampling.sampling_width = 512
    sampling.sem_seg_scale = 0.02

    # data
    config.data = data = ml_collections.ConfigDict()
    data.dataset = 'cityscapes256'
    data.image_size = 256
    data.random_flip = False
    data.n_channels = 3
    data.n_labels = 20
    data.crop_to_square = False

    # model
    config.model = model = ml_collections.ConfigDict()
    model.sigma_min = 0.01
    model.sigma_max = 338
    model.n_scales = 2000
    model.beta_min = 0.1
    model.beta_max = 20.
    model.dropout = 0.
    model.embedding_type = 'fourier'
    model.bilinear = True
    model.conditional = True

    # optimization
    config.optim = optim = ml_collections.ConfigDict()
    optim.weight_decay = 0
    optim.lr = 2e-4
    optim.beta1 = 0.9
    optim.eps = 1e-8
    optim.warmup = 5000
    optim.grad_clip = 1.
    optim.mixed_prec = True

    config.device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

    return config
