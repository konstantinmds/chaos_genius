# -*- coding: utf-8 -*-
"""alert controlller."""
from chaos_genius.databases.models.alert_model import Alert


def get_alert_list(frequency: str = None, as_obj: bool = False):
    """get the list of the alerts

    Args:
        frequency (str, optional): schedular frequency for which
                alert need to tested. Defaults to None.
        as_obj (bool, optional): send the list as Alert object.
                Defaults to False.

    Returns:
        list: List of the alerts
    """
    filters = [Alert.alert_status == True]
    if frequency:
        filters.extend([Alert.alert_frequency == frequency])
    data = Alert.query.filter(*filters).order_by(Alert.id.desc()).all()
    return data if as_obj else [point.as_dict for point in data]


def get_alert_info(id: int):
    """alert info for any given alert id

    Args:
        id (int): alert id
    """
    if alert := Alert.get_by_id(id):
        return alert.as_dict
    else:
        raise Exception("Alert ID doesn't exist")
