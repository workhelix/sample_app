from boto3 import resource, client
import streamlit as st
from pyathena import connect
from typing import Optional


class AWS:
    def __init__(self, bucket: str):
        """
        Connect to AWS Object
        """

        st.write("Connecting to AWS...")
        s3 = resource('s3')

        try:
            self.bucket = s3.Bucket(bucket)
        except e:
            st.write(f"Unable to connect to bucket. Error: {e}")
            raise ValueError(e)

        st.write(f"Successfully connected to AWS Bucket '{bucket}'")


class Athena:
    def __init__(self, s3: str, region: str):
        self.s3 = s3
        self.region = region
        st.write("Connecting to Athena...")
        try:
            self.conn = connect(s3_staging_dir=self.s3, region_name=self.region).cursor()
        except e:
            st.write(f"Unable to connect to bucket. Error: {e}")
            raise ValueError(e)
        st.write(f"Successfully connected to AWS Athena")

    def execute_query(self,
              query: str,
              sql_filepath=None):
        """
        Query Table in Athena

        query: sql query
        """
        if all(v is None for v in [sql_filepath, query]):
            raise ValueError("No query or sql filepath provided")

        if sql_filepath:
            pass
        else:
            st.write("Querying Athena...")
            self.conn.execute(query)
            st.write(self.conn.fetchall())

    # def get_contents(self):
    #     # Iterates through all the objects, doing the pagination for you. Each obj
    #     # is an ObjectSummary, so it doesn't contain the body.
    #     for obj in self.bucket.objects.all():
    #         key = obj.key
    #         st.write(key)
    #         #body = obj.get()['Body'].read()



        
        
