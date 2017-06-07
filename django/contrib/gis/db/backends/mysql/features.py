from django.contrib.gis.db.backends.base.features import BaseSpatialFeatures
from django.db.backends.mysql.features import \
    DatabaseFeatures as MySQLDatabaseFeatures


class DatabaseFeatures(BaseSpatialFeatures, MySQLDatabaseFeatures):
    has_spatialrefsys_table = False
    supports_add_srs_entry = False
    supports_distance_geodetic = False
    supports_length_geodetic = False
    supports_distances_lookups = False
    supports_transform = False
    # SHIV EDITED THIS ON 07/06/17
    # to take advantage of MySQL proper ST_ functions
    # supports_real_shape_operations = False
    supports_null_geometries = False
    supports_num_points_poly = False

    # SHIV EDITED THIS ON 07/06/17
    # to take advantage of MySQL proper ST_ functions
    @property
    def supports_real_shape_operations(self):
        return self.connection.mysql_version >= (5, 6, 1)
