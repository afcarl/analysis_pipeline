#!/usr/bin/env python

import logging

import networkx
import networkx.readwrite

from .. import pipeline


def load(filename):
    """
    Shortcut function to load a edgelist file describing a pipeline graph

    Parameters
    ----------
    filename : str
        A edgelist filename

    Returns
    -------
    graph : networkx.DiGraph
        A networkx graph that describes the pipeline

    See Also
    --------
    networkx.readwrite.read_edgelist
    networkx.DiGraph
    """
    return networkx.readwrite.read_edgelist(filename, \
            create_using=networkx.DiGraph())


def parse_nodes(graph, cfg):
    """
    Load node operations defined in a cfg file

    Parameters
    ----------
    graph : networkx.DiGraph
        A networkx graph that describes the pipeline
    cfg : ConfigParser or cconfig.TypedConfig
        A config file that defines the operations in the pipeline
    """
    for node in graph.nodes_iter():
        logging.debug("parsing node: %s" % node)
        graph.node[node] = pipeline.operation.parse_node(cfg, node)
