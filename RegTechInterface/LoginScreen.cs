using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace RegTechInterface
{
    public partial class LoginScreen : Form
    {
        public LoginScreen()
        {
            InitializeComponent();
            
        }

        
        private void btn_Login_Click(object sender, EventArgs e)
        {
            if (txt_UserName.Text == "" || txt_Pass.Text == "")
            {
                MessageBox.Show("Please Provide Both Username and Password","Error",MessageBoxButtons.OK,MessageBoxIcon.Information);
                return;
            }

            try
            {
                string myquery = "Select * from DAEN690.dbo.tbl_UserCredentials where UserName='"+txt_UserName.Text+"' and UserPass='"+txt_Pass.Text+"'";

                SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["DAEN690"].ToString());
                SqlCommand comm = new SqlCommand(myquery,conn);
                
                conn.Open();

                string uid = "";
                SqlDataReader sda = comm.ExecuteReader();
                while (sda.Read())
                {
                    uid  = sda["UserID"].ToString();
                }
                
                if (!String.IsNullOrEmpty(uid))
                {
                    
                    ChapterSelection MainScreen = new ChapterSelection();
                    MainScreen.Show();
                    this.Hide();
                    
                }

                else
                {
                    MessageBox.Show("Incorrect Credentials","Error",MessageBoxButtons.OK,MessageBoxIcon.Error);
                }

                
                conn.Close();
                

            }

            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
