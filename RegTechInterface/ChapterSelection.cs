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

    public partial class ChapterSelection : Form
    {
        public ChapterSelection()
        {
            InitializeComponent();
        }

       
        private void btnChap1_Click(object sender, EventArgs e)
        {

            //List<Requirement> lst_Reqts_Chap2 = new List<Requirement>();
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();


        }

        private void btnChap2_Click(object sender, EventArgs e)
        {
            //List<Requirement> lst_Reqts_Chap2 = new List<Requirement>();
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap3_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap4_Click(object sender, EventArgs e)
        {

            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap5_Click(object sender, EventArgs e)
        {
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap6_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap7_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap8_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap9_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap10_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnChap11_Click(object sender, EventArgs e)
        {
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap12_Click(object sender, EventArgs e)
        {
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap13_Click(object sender, EventArgs e)
        {
            this.Close();
            Form1 frm = new Form1(sender);
            frm.Show();
            
        }

        private void btnChap14_Click(object sender, EventArgs e)
        {
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap15_Click(object sender, EventArgs e)
        {
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap16_Click(object sender, EventArgs e)
        {
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap17_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();
        }

        private void btnChap18_Click(object sender, EventArgs e)
        {
            
            Form1 frm = new Form1(sender);
            frm.Show();
            this.Close();

        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
            LoginScreen Login = new LoginScreen();
            Login.Show();
        }
    }


    

}
