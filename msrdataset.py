import os
import datasets

class MSRIndianSpeech(datasets.GeneratorBasedBuilder):
    """TODO: Short description of my dataset."""

    VERSION = datasets.Version("1.1.0")

    # This is an example of a dataset with multiple configurations.
    # If you don't want/need to define several sub-sets in your dataset,
    # just remove the BUILDER_CONFIG_CLASS and the BUILDER_CONFIGS attributes.

    # If you need to make complex sub-parts in the datasets with configurable options
    # You can create your own builder configuration class to store attribute, inheriting from datasets.BuilderConfig
    # BUILDER_CONFIG_CLASS = MyBuilderConfig

    # You will be able to load one or the other configurations in the following list with
    # data = datasets.load_dataset('my_dataset', 'first_domain')
    # data = datasets.load_dataset('my_dataset', 'second_domain')
    
    def _info(self):
        # TODO: This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset
        features = datasets.Features(
                {
                    "sentence": datasets.Value("string"),
                    "path": datasets.Value("string")
                }
            )
            
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description='_DESCRIPTION',
            # This defines the different columns of the dataset and their types
            features=features,  # Here we define them above because they are different between the two configurations
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=None,
            # Homepage of the dataset for documentation
            homepage='_HOMEPAGE',
            # License for the dataset if available
            license='_LICENSE',
            # Citation for the dataset
            citation='_CITATION',
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration
        # If several configurations are possible (listed in BUILDER_CONFIGS), the configuration selected by the user is in self.config.name

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLs
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive
        # my_urls = _URLs[self.config.name]
        # data_dir = dl_manager.download_and_extract(my_urls)
        
        # https://huggingface.co/docs/datasets/add_dataset.html
                
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "audios": os.path.join(self.config.data_dir, "gu-in-Train", "Audios"),
                    "transcriptions": os.path.join(self.config.data_dir, "gu-in-Train", "transcription.txt"),
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "audios": os.path.join(self.config.data_dir, "gu-in-Test", "Audios"),
                    "transcriptions": os.path.join(self.config.data_dir, "gu-in-Test", "transcription.txt"),
                    "split": "test"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "audios": os.path.join(self.config.data_dir, "gu-in-Test", "Audios"),
                    "transcriptions": os.path.join(self.config.data_dir, "gu-in-Test", "transcription.txt"),
                    "split": "dev",
                },
            ),
        ]

    def _generate_examples(
        self, audios, transcriptions, split  # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    ):
        """ Yields examples as (key, example) tuples. """
        # This method handles input defined in _split_generators to yield (key, example) tuples from the dataset.
        # The `key` is here for legacy reason (tfds) and is not important in itself.
        
        print('split: {}'.format(split))

        transDict = {}
        with open(transcriptions, 'r', encoding='utf-8') as rd:
            for line in rd.readlines():
                cols = line.split('\t')
                transDict[cols[0]] = cols[1].strip()
        
        audioDict = {}
        for audioFile in os.listdir(path=audios):
            name = audioFile.split('.')[0]
            audioDict[name] = os.path.join(audios, audioFile)

        print(len(transDict.keys()), len(audioDict.keys()))
            
        assert set(audioDict.keys()).issubset(set(transDict.keys())), "Some audio files missing transcription"
        
        for k,v in audioDict.items():
            yield k, {
                "sentence": transDict[k],
                "path": v
            }