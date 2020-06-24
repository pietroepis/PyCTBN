import pandas as pd
import numpy as np
import os
import json_importer as imp
import trajectory as tr
import structure as st


class SamplePath:
    """
    Rappresenta l'aggregazione di una o più traiettorie.
    Ha il compito dato di costruire tutte gli oggetti Trajectory a partire
    dai dataset contenuti nella directory files_path.

    :importer: l'oggetto Importer che ha il compito di caricare i dataset
    :trajectories: lista contenente le traiettorie create
    """

    def __init__(self, files_path):
        print()
        self.importer = imp.JsonImporter(files_path)
        self.trajectories = []
        self.structure = None

    def build_trajectories(self):
        self.importer.import_data()
        for traj_data_frame in self.importer.df_samples_list:
            trajectory = tr.Trajectory(self.importer.build_list_of_samples_array(traj_data_frame))
            self.trajectories.append(trajectory)
        self.importer.clear_data_frames()

    def build_structure(self):
        self.structure = st.Structure(self.importer.df_structure, self.importer.df_variables)

    def get_number_trajectories(self):
        return len(self.trajectories)

"""os.getcwd()
os.chdir('..')
path = os.getcwd() + '/data'
print(path)
sp = SamplePath(path)
sp.build_trajectories()
sp.build_structure()
print(sp.trajectories[7].actual_trajectory)
print(sp.importer.df_samples_list[7])
print(sp.get_number_trajectories())
print(list(sp.structure.list_of_edges()))"""


